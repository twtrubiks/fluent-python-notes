# A Array of Sequences  - Part 2-3

準備中

[Youtube Tutorial  - A Array of Sequences - Part 2-3](xxx)

***list.sort and the sorted Built-In Function***

**list.sort** , without making a copy.

```text
it returns None to remind us that it changes the target object, and does not create a new list.
This is an important python api convention : functions or methods that change an object an object in place should return None to make it clear to rhe caller that the object itself was changed, and no new object was created.
```

list.sort 的範例可參考 [sort.py](https://github.com/twtrubiks/python-notes/blob/master/sort.py)。

**sorted** , the built-in function sorted creates a new list and returns it ( always returns a newly created list ).

sorted 的範例可參考 [sorted.py](https://github.com/twtrubiks/python-notes/blob/master/sorted.py)。

once your sequences are sorted, they can be very efficiently searched.

可以使用 standard binary search algorithm ( bisect module ) ，

***Managing Ordered Sequences with Bisect***

```text
The bisect module offers two main functions - bisect and insort - that use the binary search algorithm to quickly find and insert items in any sorted sequence.
```

使用 bisect 時，一定要是 sorted sequence，更多說明可參考 [bisect.html](https://docs.python.org/3.6/library/bisect.html)，

```text
bisect is actually an alias for bisect_right.
bisect_right returns an insertion point after the existing item.
bisect_left returns the position of the existing item.
```

看下面的例子，

```python
>>> import bisect
>>> Y = [0, 2, 2, 3, 6, 8, 12, 20]
>>> x_insert_point = bisect.bisect_left(Y, 2)
>>> x_insert_point
1
>>> x_insert_point = bisect.bisect_right(Y, 2)
>>> x_insert_point
3
>>> x_insert_point = bisect.bisect(Y, 2) # bisect is actually an alias for bisect_right
>>> x_insert_point
3
```

教大家一個比較簡單的方法， bisect_left  從左邊看，bisect_right 則從右邊看。

再來看 `bisect.insort_right` 以及 `bisect.insort_left` ，其實它就是包含上面 ( `bisect.bisect` ) 的特性再加上 insert。

```python
>>> import bisect
>>> Y = [0, 2, 2, 3, 6, 8, 12, 20]
>>> x_insort_left = bisect.insort_left(Y, 2)
>>> Y
[0, 2, 2, 2, 3, 6, 8, 12, 20]
>>> Y = [0, 2, 2, 3, 6, 8, 12, 20]
>>> x_insort_right = bisect.insort_right(Y, 1) # bisect.insort is actually an alias for bisect.insort_right
>>> Y
[0, 1, 2, 2, 3, 6, 8, 12, 20]
```

fluent python 中 bisect 的範例 [eg_2_17.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Array_of_Sequences_part_3/eg_2_17.py)

```python
python eg_2_17.py
```

或是

```python
python eg_2_17.py left
```

在 [官方文件](https://docs.python.org/3/library/bisect.html#other-examples) 中的範例，

Given a test score, grade returns the corresponding letter grade ,

```python
>>> import bisect
>>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
...         i = bisect.bisect(breakpoints, score)
...         return grades[i]
...
>>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
['F', 'A', 'C', 'C', 'B', 'A', 'A']
```

fluent python 中 Insort 的範例 [eg_2_19.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Array_of_Sequences_part_3/eg_2_19.py) ( Insort keeps a sorted sequence always sorted. )

***Arrays***

[array](https://docs.python.org/3/library/array.html)

```text
If the list will only contain numbers, an array.array is more efficient than a list: it support all mutable sequence operations ( including .pop, .insert, and .extend ) , and additional methods for fast loading and saving such as .frombytes and .tofile.
```

python will not you put any number that does not match the type for the array.

看下面的例子，

```python
>>> from array import array
>>> array('b', ((999,2,3))) # 'b' is signed char
Traceback (most recent call last):
  File "<input>", line 1, in <module>
OverflowError: signed char is greater than maximum
```

'b' 為 typecode ，上面的 array 就只能放 signed char ( -128 to 127 )，放其他的 type 就會 error。

其他的 typecode 說明，可參考 [array](https://docs.python.org/3/library/array.html)。

fluent python 中的例子， Creating , saving and loading a large array of 10 floats

```python
>>> from array import array
>>> from random import random
>>> floats = array('d', (random() for i in range(10 ** 7))) #  'd' is double float
>>> floats[-1]
0.3937325241174071
>>> fp = open('floats.bin', 'wb')
>>> floats.tofile(fp)
>>> fp.close()
>>> floats2 = array('d')
>>> fp = open('floats.bin', 'rb')
>>> floats2.fromfile(fp, 10 ** 7)
>>> fp.close()
>>> floats2[-1]
0.3937325241174071
```

從上面的例子你可以發現，`array.tofile` 和 `floats2.fromfile` 很容易使用，速度也快，

如果將上面改存成 text file，你會發現存成 binary file 節省非常多的空間。

還有一個也可以 pickle module 也可以參考。

Another fast and more flexible way of saving numeric data is the [pickle module](https://docs.python.org/3/library/pickle.html) for object serialization.
it handles almost all built-in types.

範例可參考 [pickle_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/pickle_tutorial.py)

***Memory View***

[memoryview](https://docs.python.org/3/library/stdtypes.html#memoryview)

```text
The built-in memoryview class is a shared-memory sequence type that lets you handle slices of arrays without coping bytes. It was inspired by the NumPy library.
```

如果你想進一步的了解，可參考 [When should a memoryview be used](https://stackoverflow.com/questions/4845418/when-should-a-memoryview-be-used/)

```text
A memoryview is essentially a generalized NumPy array structure in Python itself (without the math). It allows you to share memory between data-structures (things like PIL images, SQLlite data-bases, NumPy arrays, etc.) without first copying. This is very important for large data sets.

With it you can do things like memory-map to a very large file, slice a piece of that file and do calculations on that piece (easiest if you are using NumPy).
```

先來看個例子，

not use memoryview

```python
>>> # not use memoryview
>>> a1 = bytearray('abcde'.encode())
>>> b1 = a1[:2]  # generate new str , does not affect a1
>>> a1
bytearray(b'abcde')
>>> b1
bytearray(b'ab')
```

為什麼這這邊我不直接使用 str 就好，而要使用 bytearray :question:

原因是在 [A Array of Sequences - Part 2-1](https://github.com/twtrubiks/fluent-python-notes/tree/master/A_Array_of_Sequences_part_2_1) 有提到 ，

str is immutable sequences , bytearray is mutable sequences.

如果改成 str 就會出現 error ( 如下範例 )

```python
>>> a1 ='abcde'.encode()
>>> ma1 = memoryview(a1)
>>> mb2 = ma1[:2]
>>> mb2[:2] = 'bb'.encode()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: cannot modify read-only memory
```

use memoryview

```python
>>> # use memoryview
>>> a2 = bytearray('abcde'.encode())
>>> ma2 = memoryview(a2)
>>> mb2 = ma2[:2]  # not generate new str
>>> mb2[:2] = 'bb'.encode()
>>> mb2.tobytes() # affect ma2
b'bb'
>>> ma2.tobytes()
b'bbcde'
```

***NumPy and SciPy***

For advanced array and matrix operations.

如果你有很大量的陣列以及要進去矩陣的操作，建議使用 NumPy 會更好，這邊就不在另外做介紹，

因為這個非常深的東西:relaxed:

***Deques***

```text
The .append and .pop methods make a list usable as a stack or a queue ( if you use .append and .pop(0), you get LIFO behavior ).But inserting and removing from the left of a list ( the 0-index end ) is costly because the entire list must be shifted.
```

雖然 list 很好用，可以透過  .append and .pop(0) 的方法完成  LIFO ( Last in First out - 後進先出 )，但不管是

從 list 中的最左邊 ( 0-index ) inserting 還是 removing 付出的成本都很高，所以，如果你有 LIFO 的需求，使用

deques 會更好:smile:

```text
The class collections.deque is a thread-safe (synchronized) double-ended queue designed for fast inserting and removing from both ends.
Deque is safe to use as a LIFO queue in multithreaded applications without the need for using locks.
```

fluent python 中的例子

```python
>>> from collections import deque
>>> dq = deque(range(10), maxlen=10)
>>> dq
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> # rotating with n > 0 takes items from the right end and prepends then to the left ;
>>> # when n < 0 items are taken from left and appended to the right
>>> dq.rotate(3)
>>> dq
deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
>>> dq.rotate(-4)
>>> dq
deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], maxlen=10)
>>> # when it is full , it discards items from the opposite end when you append new ones
>>> dq.appendleft(-1)
>>> dq
deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> # deque.extend( iterable )
>>> dq.extend([11, 22, 33])
>>> dq
deque([3, 4, 5, 6, 7, 8, 9, 11, 22, 33], maxlen=10)
>>> dq.extendleft([10, 20, 30, 40])
>>> dq
deque([40, 30, 20, 10, 3, 4, 5, 6, 7, 8], maxlen=10)
```

## 執行環境

* Python 3.6.4

## Reference

* [fluentpython/example-code](https://github.com/fluentpython/example-code)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)
