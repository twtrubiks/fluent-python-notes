# What is the Hashable

[Youtube Tutorial - What is the Hashable]( https://youtu.be/-Qw3V2VoEQg)

這篇文章主要會介紹 **Hashable**，

以下為 fluent python 中的一段說明，

```text
An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__() method),
and can be compared to other objects (it needs an __eq__() method). Hashable objects which compare equal must have
the same hash value.
```

假如一個物件是 hashable，那麼在他的生命週期中，會有一個固定不變的 hash 值 ( 需要 `__hash__()` method)，

而且可以和其他的物件比較 ( 需要 `__eq__()` method )。

假如兩個物件相等，hashable objects 需要有相同的 hash 值才算是相等。

immutable types ( tuple, str, and bytes ) are all hashable.

上面這句話沒有完全正確，來看一個例子，

```python
>>> t1 = (1 , 2 , (30, 40)) # <1>
>>> hash(t1)
1350807749
>>> t2 = (1 , 2 , [30, 40]) # <2>
>>> hash(t2)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
```

<1> 的部分沒什麼問題，他是 hashable。

<2> 的部分就有問題了，出現 error message，並且告訴你，

list 是 unhashable ( 因為 list 是 mutable )，也就是說，

假如 tuple 裡面全部都是 immutable，這樣他就是 hashable，

但假如 tuple 裡面有包含 mutable ( 像是 <2> 的部分 )，

這樣他就是 unhashable。

補充，mutable types

```text
list, bytearray, array.array, collections.deque, and memoryview.
```

如果想了解更多，可參考我之前的文章 [An Array of Sequences - Part 2-1](https://github.com/twtrubiks/fluent-python-notes/tree/master/A_Array_of_Sequences_part_2_1)。

mutable 都是 unhashable，

```python
>>> a = [1,2,3]
>>> hash(a)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: unhashable type: 'list'
```

所以前面才會和大家說，`immutable types are all hashable.`

這句話沒有完全正確。

python [hashable](https://docs.python.org/3/glossary.html#term-hashable) 文件中有一段說明，

```text
Objects which are instances of user-defined classes are hashable by default.
They all compare unequal (except with themselves), and their hash value is derived from their id().
```

使用者自己定義的 class 的 instances 都是 hashable，因為是從 `id()` 中取回，

看下面的例子，

```python
>>> class A:
...     pass
...
>>> a = A()
>>> hash(a) # <1>
3660815
>>> id(a) # <2>
58573040
```

有沒有發現 <1> 和 <2> 的部分不相同，在舊版的 python 中，他們會是相等的，

但是後來的版本會是 `hash(a) == id(a)/16`，原因是 CPython 裡面的 id 都是 16 的倍數，

相關來源可參考 [here](https://stackoverflow.com/questions/11324271/what-is-the-default-hash-in-python)。

在 Python 中，dict 的 key 一定要是 hashable，主要是因為 dict 內部的實作，至於實作的部分，

就要談到 hash table，這部分又要談很久，所以留到下次介紹:smile:

延伸閱讀，利用 Hash Table 解題目，可參考 [Two_Sum_001.py](https://github.com/twtrubiks/leetcode-python/blob/master/Two_Sum_001.py)

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
