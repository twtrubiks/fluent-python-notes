# A Array of Sequences - Part 2-1

[Youtube Tutorial  - A Array of Sequences - Part 2-1](https://youtu.be/FD4kmQt0-RY)

基本上，sequences 分為兩種，

***container sequences***

```text
list, tuple, and collections.deque can hold items of different types.
```

***flat sequences***

```text
str, bytes, bytearray, memoryview, and array.array hold items of one type.
```

另外一種區分的方法是藉由 mutability

***Mutable sequences***

```text
list, bytearray, array.array, collections.deque, and memoryview.
```

***Immutable sequences***

```text
tuple, str, and bytes.
```

***List Comprehensions ( listcomps ) and Generator Expressions ( genexps )***

先來講 **List Comprehensions**

還記得在 [之前](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Pythonic_Card_Deck/README.md) 提到的這段 code 嗎 :question:

```python
>>> [str(n) for n in range(2, 11)]
['2', '3', '4', '5', '6', '7', '8', '9', '10']
```

上面這就是很典型的 listcomps，這段程式碼，相等於

```python
>>> seqs=[]
>>> for n in range(2,11):
...     seqs.append(str(n))
>>> seqs
['2', '3', '4', '5', '6', '7', '8', '9', '10']
```

應該非常的明顯，前者可讀性好很多，而且 code 也少了很多行， 接著再看一個例子，

```python
>>> colors = ['black', 'white']
>>> sizes = ['S', 'M', 'L']
>>> tshirts = [(color, size) for color in colors for size in sizes] # 第一種寫法
>>> tshirts = [(color, size) for color in colors # 第二種寫法 ( 也可以換行 )
...            for size in sizes]
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
>>>
>>> ## 上方這段程式碼，相等於下方
>>>
>>> tshirts = []
>>> for color in colors:
...       for size in sizes:
...         tshirts.append((color, size))
...
>>> tshirts
[('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
```

相信大家看完就會了解 [之前](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Pythonic_Card_Deck/README.md) 此部分的 code，

```python
self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
```

接著我們來看 **Generator Expressions ( genexps )**

```text
To initialize tuples, arrays, and other types of sequences, you could also start from a
listcomp,but a genexp saves memory because it yields items one by one using the iterator
protocol instead of building a whole list just to feed another constructor.
```

使用 genexp 可以節省記憶體。

```python
>>> genexps = (str(n) for n in range(2, 11)) # <1>
>>> genexps # <2>
<generator object <genexpr> at 0x00000213C7F2C468>
>>> tuple(genexps)
('2', '3', '4', '5', '6', '7', '8', '9', '10')
```

**1** 的部份和 listcomps 寫法唯一不一樣的地方就是，

listcomps 是使用 `[`  `]` 這個符號， 而 genexps 則是使用 `(`  `)` 這個符號。

**2** 的部分是要讓大家了解，它是一個 generator object 。

剛剛說 genexp 可以節省記憶體，讓我們透過數據說話，如下，

```python
>>> from sys import getsizeof # Return the size of an object in bytes.
>>> list_comp = [x for x in range(1000000)]
>>> gen_exp = (x for x in range(1000000))
>>> getsizeof(list_comp)
8697464
>>> getsizeof(gen_exp)
88
```

接下來我們來談談 `tuples`

```text
Tuples do duuble duty : they can be used as immutable lists and also as record with no field names.
```

先來看 immutable lists

```python
>>> tuples = (1,3)
>>> tuples[0]
1
>>> tuples[0] = 2
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

再來看 Tuples as record with no field names.

( 咦? 是不是有似曾相識的感覺，沒錯，我們在 [這裡](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Pythonic_Card_Deck/README.md) 有提到 )

namedtuple 就如同一筆 record，可參考 [namedtuple_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/namedtuple_tutorial.py)

```python
>>> name_ids = [('name1',1),('name2',2),('name3',3)] # Tuples as record with no field names.
>>> for name, _ in name_ids: # <1> Unpacking
...     print(name)
...
name1
name2
name3
```

**1** 的這部分我只希望顯示 name ( 不管 id )，所以我將 id 的部份使用了一個 `_` ( dummy variable )，

關於 `_` 額外補充一下，如果你有使用到多國語系，就會使用到 [gettext module](https://docs.python.org/3/library/gettext.html) ，

這時候 `_` 可能就不是一個很適合的 dummy variable。

Unpacking 是什麼 ?

```python
>>> name_pk = ('name1',1)
>>> name , pk = name_pk # tuple unpacking
>>> name
'name1'
>>> pk
1
```

tuple unpacking 這個特性，讓我們想要交換兩個變數時，可以直接這樣寫

( 大家如果有摸過 C 語言就知道，要用一個 temp 的變數 )

```python
b, a = a, b # without using a temporary variable
```

超簡單快速

***using * to grab excess items***

這個是 python3 才有的功能，可參考 [new-syntax](https://docs.python.org/3.0/whatsnew/3.0.html#new-syntax)，

官方說明為 Extended Iterable Unpacking，直接看範例，會更快了解

```python
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
>>> *head, b, c, d = range(5)
>>> head, b, c, d
([0, 1], 2, 3, 4)
```

***Slice***

`seq[start,stop,step]`

```python
>>> s = 'abcdefg'
>>> s[::2]
'aceg'
>>> s[::-1]
'gfedcba'
>>> s[2::2]
'ceg'
```

這其實在 [這裡](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Pythonic_Card_Deck/README.md) 也有提到，也就是 `deck[12::13]`。

當執行 `seq[start,stop,step]` 時，其實 python 是去 call `seq.__getitem__( slice(start, stop, step ))`

```python
>>> slice
<class 'slice'>
>>> dir(slice)
[..., 'indices', 'start', 'step', 'stop']
```

indices 它讓 slice 變的強大，它可以幫我們 normalized，保持你適合的長度，看下面的例子

```python
>>> s = 'abcdefg'
>>> len(s)
7
>>> s[0:7:2]
'aceg'
>>> s[:100:2]
'aceg'
>>> s[2:7:1]
'cdefg'
>>> s[-5:]
'cdefg'
```

就是因為 indices 的原因，讓 `s[0:7:2]` 和 `s[:100:2]` 以及 `s[2:7:1]` 和 `s[-5:]` 結果相同。

Assigning to Slice

```python
>>> seqs = list(range(10))
>>> seqs
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> seqs[2:5] = [20, 30]
>>> seqs
[0, 1, 20, 30, 5, 6, 7, 8, 9]
>>> del seqs[5:7]
>>> seqs
[0, 1, 20, 30, 5, 8, 9]
>>> seqs[2:5] = 100
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: can only assign an iterable
>>> seqs[2:5] = [100] # must be an iterable object
>>> seqs
[0, 1, 100, 8, 9]
```

## 執行環境

* Python 3.6.4

## Reference

* [fluentpython/example-code](https://github.com/fluentpython/example-code)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)
