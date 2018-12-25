# What is the Monkey Patch

[Youtube Tutorial - 認識 Monkey Patch in Python - part 1](https://youtu.be/eJXSIbEJIXo)

[Youtube Tutorial - 認識 Monkey Patch in Python - part 2](https://youtu.be/4FRGP7iRsM0)

[Youtube Tutorial - 認識 Monkey Patch in Python - part 3](https://youtu.be/JRCPzue4sFU)

這篇文章主要會介紹 **Monkey Patch**，

中文的意思我就不翻譯了，簡單說，你可以把它想成是一種補丁，

可以將 runtime ( 執行中 ) 的程式，動態的改變 class or module or function，

且不需要修改 source code，通常使用在增加功能 ( 暫時性 ) 和修正 bugs。

來看一個例子，

[demo1.py](demo1.py)

```python
class A:
    def speak(self):
        return "hello"

def speak_patch(self):
    return "world"

A.speak = speak_patch # <2>
some_class = A()
print('some_class.speak():', some_class.speak()) # <1>
```

<1> 的部分會顯示 `world`，而不會顯示 `hello`，原因是因為我們在 <2> 的部分

將它 Monkey Patch 了，使用 `speak_patch` 這個 function 去取代掉原來的 `speak`。

再來看一個例子，

[demo2.py](demo2.py)

```python
class A:
    def __init__(self, array):
        self._list = array

    # def __len__(self): # <2>
    #     return len(self._list)

def length(obj): # <1>
    return len(obj._list) # <2>


A.__len__ = length # <3>

a = A([1, 2, 3])
print('length:', len(a))
```

A class 並沒有實作 `__len__` 的方法 ( 將 <2> 註解起來 )，如果是在 runtime 中，

我們可不可以把 `__len__` 方法實作上去:question:

可以，只要將 <1> 的部分的 function 先寫出來，記得，該有的參數還是要有，但名稱可以

不一樣，像是原本 <2> 是 self，在 <1> 可以任意寫 ( 例如 obj )，因為會在 <3> 的部分

自己去 mapping 起來，但是取長度時，也就是 <2> 的部分，就必須要寫 `obj._list`，

重點是後面的 `_list` 屬性。

經過以上的部分，就可以成功的在 runtime 時，實作 A class 的 `__len__`，這邊你可能

會問我，那為什麼不一開始就實作 `__len__` 就好，像是，

```python
class A:
    def __init__(self, array):
        self._list = array

    def __len__(self): # <2>
        return len(self._list)
```

原因是可能我們不希望去修改 A class 的 source code，而這修改也只是暫時性的，像是

測試之類的。

順帶一提，

其實它打破了 encapsulation ( 封裝 ) 的概念， 而且傾向於緊密耦合 ( tightly coupled )

，也就是破壞 SOLID 的概念 ( SOLID 關鍵字 GOOGLE 就可以能到很多說明 )。

所以他是暫時的解決方法，對於整個 code 的整合，並不是一個推薦的技術。

[Youtube Tutorial - 認識 Monkey Patch in Python - part 2](https://youtu.be/4FRGP7iRsM0)

Python 中的 Monkey Patch 是有限制的，它限制你不能 patched built-in types，

舉個例子，假如我今天想要 patched str 這個物件，

[demo3.py](demo3.py)

```python
def find(self, sub, start=None, end=None):
    return 'ok'

str.find = find
```

你會發現得到 error messages，這個限制我覺得不錯，為什麼呢:question:

原因是可以保證 built-in types 的功能都是原本的，避免有人去 patched 它之後，

導致後續一堆奇怪的問題。

記得，Monkey Patch 不能濫用，否則會造成系統難以維護以及 code 很難理解

( 因為你東 patched 一個，西 patched 一個，誰看得懂 :triumph:)

回頭再來看 [demo1.py](demo1.py)，

```python
class A:
    def speak(self):
        return "hello"

def speak_patch(self):
    return "world"

A.speak = speak_patch # <2>
some_class = A()
print('some_class.speak():', some_class.speak()) # <1>

some_class2 = A()
print('some_class2.speak():', some_class2.speak()) # <3>
```

注意 <3> 的部分，會顯示 world ，而非 hello，因為他已經被 patched，

除非你把它重新 patched 回來，因為這個特性，所以絕對不能濫用，

不然使用者會覺得很奇怪，不是應該要輸出 hello 嗎:question:

但是卻是輸出 world。

動態修改 class or module or function 的這個特性，和 dessign patterns 中的

adapter 類似 ( 可以先把他想成是變壓器的概念 )，只不過在 adapter 中，是

實作一個全新的 Adapter class 來處理同一個問題。

以後我會在介紹 adapter，可先參考 [python-patterns-adapter.py](https://github.com/faif/python-patterns/blob/master/structural/adapter.py)。

python 中的 `gevent` module 也有使用到 Monkey Patch 的特性。

[Youtube Tutorial - 認識 Monkey Patch in Python - part 3](https://youtu.be/JRCPzue4sFU)

這邊補充一下，`types` module 中的 `types.MethodType`

很類似 Monkey Patch，來看一個 `types.MethodType` 的例子，

[demo4.py](demo4.py)

```python
import types

class A:
    def speak(self):
        return "hello"

def speak_patch(self):
    return "world"

a = A()
a.speak = types.MethodType(speak_patch, a) # <1>
print('a.speak():', a.speak()) # <2>

a2 = A()
print('a2.speak():', a2.speak()) # <3>
```

<1> 的部分，使用方法 `types.MethodType( fun, obj)`，這邊要注意的是，

我們是放一個 instance (a) 進去，所以 <2> 的輸出是 world，而 <3> 的

輸出則是 hello ( 因為 a2 的 instance 我們並沒有去修改 )。

再來看一個例子，

[demo5.py](demo5.py)

```python
import types

class A:
    def speak(self):
        return "hello"

def speak_patch(self):
    return "world"

A.speak = types.MethodType(speak_patch, A) # <1>
a = A()
print('a.speak():', a.speak()) # <2>

a2 = A()
print('a2.speak:', a2.speak()) # <3>
```

<1> 的部分，我們是方一個 A class 進去，所以 <2> 和 <3> 的輸出

都會是 world，因為我們改變了 A class，這幾乎就和前面所介紹的

Monkey Patch 是一樣的功能。

這邊主要是強調 patched instance ( [demo4.py](demo4.py) ) 或是

patched class ( [demo5.py](demo5.py) ) 是不太一樣的。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
