# What is the Python GIL

[Youtube Tutorial - What is the Python GIL](https://youtu.be/weqxMa-tBfQ)

**Cpython** ( 大多數我們看到的 Python 或是你正在使用的 Python 都是 Cpython ) 不是一個 thread-safe，

所以我們需要一個 GIL ( 全名為 Global Interpreter Lock )，主要是為了資料的完整性以及安全性才會有 GIL

的存在，換句話說，在同時間內，只能有一個 thread 執行 Python bytecodes ( 可參考 [dis module](https://docs.python.org/3/library/dis.html) )，

如果想更了解 [dis module](https://docs.python.org/3/library/dis.html)，可參考 [An Array of Sequences - Part 2-2](https://github.com/twtrubiks/fluent-python-notes/tree/master/A_Array_of_Sequences_part_2_2) 這篇。

這就是有時候你可能會聽到別人說 Python 因為 GIL 的關係導致很慢的原因

( 但這邊要注意，是 CPython interpreter 的關係，並不是 Python 本身的關係，像是 Jython 以及 IPython

就沒有 GIL，所以開頭特別強調 CPython )。

一般來說，在寫 Python code 的時候，我們不會去控制 GIL，但當執行一些非常耗時的任務時，像是

built-in function 或一些額外用 C 寫的功能就會去釋放 GIL，事實上，用 C 寫的 Python library 可以管理 GIL，

但因為較為複雜，所以大部分的開發者不會去寫。

全部的 standard library function 實現 blocking I/O 時 ( 等待 OS 的 response ) 釋放 GIL ( 當你擁有 GIL 這把鎖的時候，

你才能執行 Python bytecodes，你可以將 GIL 想成是一張通行證 :smiley: )，也就是說 Python 是 I/O bound，當一個

thread 在等待網路的 response 時，這個 blocked I/O function 就會釋放 GIL 給其他的 thread，像是執行 `time.sleep()`

function 時會釋放 GIL。

接下來我們思考另一個問題，這邊大家可以先泡杯咖啡:relaxed:

一個 CPU ( 單核心 ) 執行一個 thread，那今天假如我有四核心，這樣是不是一次可以執行四個 thread :question:

也就是執行速度快四倍:confused:

在 Python 的世界中，答案是快沒多少，甚至多核心可能更慢 ( 也更浪費 )。

為什麼在 Python 中會這樣呢:question: 主要還是因為 GIL 的關係，

先來看一段 code ( [thread_demo](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_python_GIL/thread_demo.py) )，使用電腦的核心數作為 thread 的數量，

```python
from threading import Thread
import os


def loop():
    i = 0
    while True:
        i += 1


def main():
    print('start')
    for _ in range(os.cpu_count()):
        t = Thread(target=loop)
        t.start()


if __name__ == '__main__':
    main()
```

執行結果如下，

![alt tag](https://i.imgur.com/KyGkDjD.png)

有沒有很奇怪，理論上，CPU 應該要跑到 100 % 才對，可是它卻沒有 :question:

也就是沒有有效的利用多核心的優勢，儘管你是多核心，執行起來卻像是單核心。

先來看單核心的情況，當主 thread 達到 **閾值** 釋放 GIL 時，被喚醒的 thread 可以很順利的拿到 GIL 並執行

Python bytecodes。

但當多核心的時候就會有問題，當主 thread ( CPU0 ) 達到 **閾值** 釋放 GIL 時，其他 CPU 上的 thread 被喚醒後

開始搶這個GIL ，但有時候，主 thread ( CPU0 ) 又拿到 GIL，所以導致其他被喚醒的 thread 白白浪費 CPU 時間在

那邊等待，然後又睡著，接著又被喚醒，這種惡性循環，也就是 thrashing，而且切換 GIL 的成本是很高的。

所以就算你的 CPU 有八核心，在 Python 中，一次還是只能運作在一個核心上 ( 因為 GIL ):expressionless:

補充說明閾值，在 Python2 中是執行 1000 個 bytecodes 釋放 GIL，而在 Python3 中則是執行超過 15ms 釋放 GIL。

那我如果真的想要有效的利用多核心我該怎麼做呢:confused:

這時候可以使用 process，process 不會有 GIL 的問題，因為各個 process 之間有自己獨立的 GIL，所以不會互相

爭搶，我們來看一段 code ( [process_demo](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_python_GIL/process_demo.py) ) ，使用電腦的核心數作為 process 的數量，

```python
from multiprocessing import Process
import os


def loop():
    i = 0
    while True:
        i += 1


def main():
    print('start')
    for _ in range(os.cpu_count()):
        t = Process(target=loop)
        t.start()


if __name__ == '__main__':
    main()
```

執行結果如下，

![alt tag](https://i.imgur.com/6DTRH5B.png)

CPU 的確衝到了 100 %，也就是成功的利用了多核心的優勢，並且不受 GIL 的影響。

以下小結論，

當有高 CPU ( CPU-bound ) 計算的工作時，我們使用 [Multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html)。

當有大量 I/O ( I/O-bound ) 的工作時，我們使用 [Threading](https://docs.python.org/3/library/threading.html)，像是爬蟲。

## 執行環境

* Python 3.6.4

## Reference

* [fluentpython/example-code](https://github.com/fluentpython/example-code)
* [Grok the GIL: How to write fast and thread-safe Python](https://opensource.com/article/17/4/grok-gil)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)
