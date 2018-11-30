# An Array of Sequences  - Part 2-2

[Youtube Tutorial  - An Array of Sequences - Part 2-2](https://youtu.be/g1_XjMMB60s)

***A += Assignment Puzzler***

```python
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
```

What happens next :question: Choose the best answer:

```text
a.  t becomes (1, 2, [30, 40, 50, 60])
b.  TypeError is raised with the message 'tuple' object does not support item assignment.
c.  Neither
d.  Both a and b.
```

選 **a** 的人很明顯是對 tuple 不夠了解 ( 請前往 [上一篇](https://github.com/twtrubiks/fluent-python-notes/tree/master/A_Array_of_Sequences_part_2_1) 文章複習 )，tuple 是 immutable sequences，

但你可能會反駁我說，可是它是在 list 裡面耶:triumph: 關於這個問題，我等等和大家解答。

選 **b** 的人，代表你了解 tuple，恭喜你，但還是錯的:smirk:

讓我們用 Python console 執行看看

```python
>>> t = (1, 2, [30, 40])
>>> t[2] += [50, 60]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t
(1, 2, [30, 40, 50, 60])
```

所以答案是 **d** ( 選 **a** 或 **b** 的都各對一半 :laughing: )

可以透過 [Python Tutor](http://www.pythontutor.com/) 這個網站幫我們視覺化 Python 執行的細節。

如果你不懂如何操作，請點選我文章最前面的 [教學影片](https://youtu.be/g1_XjMMB60s)，

我們還可以透過 Python btyecode，可參考官方文件 [dis module](https://docs.python.org/3/library/dis.html)

```python
>>> dis.dis('s[a] += b')
  1           0 LOAD_NAME                0 (s)       # <1>
              2 LOAD_NAME                1 (a)       # <2>
              4 DUP_TOP_TWO                          # <3>
              6 BINARY_SUBSCR                        # <4>
              8 LOAD_NAME                2 (b)       # <5>
             10 INPLACE_ADD                          # <6>
             12 ROT_THREE                            # <7>
             14 STORE_SUBSCR                         # <8>
             16 LOAD_CONST               0 (None)
             18 RETURN_VALUE                         # <9>
```

上面的左上角的 1 代表是行數，先來看一下幾個定義，

```text
the top of the stack  - ( TOS )
the second top-most stack item ( TOS1)
the third  top-most stack item (TOS2 )
```

大家可以對照我做的這張圖，我理解 [dis module](https://docs.python.org/3/library/dis.html) 的是這樣，

如果有錯，在請糾正:smile:

![tag](https://i.imgur.com/XwNBbgl.png)

可搭配下面的說明

**1** 的部份，Pushes the value associated with co_names[namei] onto the stack.

**3** 的部份，Duplicates the two references on top of the stack, leaving them in the same order.

**4** 的部份，Implements TOS = TOS1[TOS]. ( TOS = s[a] )

**6** 的部份，Implements TOS = TOS1 + TOS. (  TOS = s[a] + b )

**7** 的部份，Lifts second and third stack item one position up, moves top down to position three.

**8** 的部份，Implements TOS1[TOS] = TOS2. (   s[a]  = s[a] + b)，我們在這邊的時候 **ERROR** 了，原因是因為它是 immutable。

**9** 的部份，Returns with TOS to the caller of the function.

通過這個例子，可以學習到幾個重點，

1. Putting mutable items in tuples is not a good idea.
2. Augmented assignment is not an atomic operation - we just saw it throwing an exception after doing part of its job.
3. Inspecting Python bytecode is not too difficult, and is often helpful to see what is going on under the hood.

簡單翻譯

1. 將 mutable items 放在 tuples 中不是很理想 (會發生神奇的問題 )。
2. Augmented assignment 不是如同一個原子 ( 不可切割 ) 的操作，它只會執行到有問題時，然後丟出一個 exception。
3. 學習觀看 Python bytecode ，雖然我也花了一點時間研究:laughing:

最後補充一下，其實只要將 `t[2] += [50, 60]` 改成 `t[2].extend([50, 60])` 就可以正常 work:thumbsup:

`t[2] += [50, 60]` 會有問題主要是因為它會企圖將值指回去 tuple ( 可參考 `__iadd__`) ，所以導致錯誤，

而 `t[2].extend([50, 60])` 之所以不會有問題，則是因為在 python 中主要是參考 ( reference ) 的概念 ( 以後會講 )，

而他也不知道它自己在 tuple 中，也不會像 `__iadd__` 會企圖將值指回去 tuple，所以正確 work。

如果你想更進一步的了解，可參考官方的說明 [Why does a_tuple[i] += [‘item’] raise an exception when the addition works](https://docs.python.org/3/faq/programming.html#why-does-a-tuple-i-item-raise-an-exception-when-the-addition-works)。

## 執行環境

* Python 3.6.4

## Reference

* [fluentpython/example-code](https://github.com/fluentpython/example-code)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)
