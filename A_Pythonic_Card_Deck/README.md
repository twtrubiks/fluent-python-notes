# A Pythonic Card Deck

[Youtube Tutorial  - A Pythonic Card Deck](https://youtu.be/ofZkuxnA2rI)

詳細程式碼可搭配 [eg_1_1.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/A_Pythonic_Card_Deck/eg_1_1.py) 安心服用:smirk:

**<1>** 的用法可參考 [random_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/random_tutorial.py)

**<2>** 的用法可參考 [namedtuple_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/namedtuple_tutorial.py)

**<3>** 說明

在 python3 中，可以直接寫

```python
class FrenchDeck:
    pass
```

而在 python2 中，則必須要寫

```python
class FrenchDeck(object):
    pass
```

如果沒有特殊需求，用 python 3 吧:smile:

**<4>** 說明

這邊建議大家可以直接用 Python Console 玩玩看

```cmd
>>> [str(n) for n in range(2, 11)]
['2', '3', '4', '5', '6', '7', '8', '9', '10']
```

先知道他可以這樣用就好，未來的介紹會再進一步的介紹他。

range 的用法可參考 [range.py](https://github.com/twtrubiks/python-notes/blob/master/range.py)，

你可能會問為什麼 range(2, 11) 不包含 11 呢 ?

***Why Slices and Range Exclude the Last Item ?***

slices [下一篇](xx)介紹會說明，這裡我們先看 range 就好，

```text
The Pythonic convention of excluding the last item in slices and ranges works well with the zero-based indexing used in Python, C, and many other languages.
```

由於上面的原因，所以有一些特性，

1. 像是 range(10)，我們很快的就可以知道它的長度是 10。

2. 當你有 start 和 stop 時，也可以很快的知道長度，像是 range(2, 11)，11-2 = 9。

3. 不用擔心 overlapping 的問題，看下面的例子

```python
>>> seqs = list(range(10))
>>> seqs
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> seqs[:2]
[0, 1]
>>> seqs[2:]
[2, 3, 4, 5, 6, 7, 8, 9]
```

將字串轉成 list。

```cmd
>>> list('JQKA')
['J', 'Q', 'K', 'A']
```

**<5>** 說明

`__init__` 就是 python 中所謂的 special methods，

當一個物件被建立時，`__init__` 就會被 invoke，像是

```cmd
>>> deck = FrenchDeck()
>>> deck
<eg_1_1.FrenchDeck object at 0x0000016B0ACD35C0>
```

deck 是一個 instance。

這邊一定會有人問，`__init__` 要怎麼唸 :question:

難道是唸 double underscores init :question:

不過這樣的話像是 private attribute `self.__x` 不就衝突了嗎:question:

又或是我們唸 double underscores init double underscores :question:

還是我們唸 double under init double under :question:

天啊，唸完我都覺得我快不行惹:triumph:

所以，這邊提供大家一個唸法，

你可以唸 dunder-init ( dunder methods ) 。

這邊提醒大家，既然它都被叫做 special methods，

就不要隨便自己定義 `__foo__`，因為未來有一天他可能會被定義。

**<6>** 說明

`self._cards` 這邊可以先把他想成類似 java 中的 protected attribute，

字面上也很明顯了，受保護的屬性，雖然我們還是可以讀到他，但不建議這樣使用 ( 如下 )

```python
>>> deck = FrenchDeck()
>>> deck._cards
[Card(rank='2', suit='spades'), Card(rank='3', suit='spades').....]
```

如果你今天看到的是 `self.__cards` ( double-underscore )，則是 private attribute。

詳細的 `protected` 以及 `private` attributes 之後的文章會有進一步的介紹，

這邊先有個概念即可:relaxed:

簡單說明一下下方的 code，

```python
self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]
```

相等於

```python
self._cards = []
for suit in self.suits:
    for rank in self.ranks:
        self._cards.append(Card(rank, suit))
```

因為 python 的特性，才能有前者的這種寫法。

**<7>** 說明

一樣是 special methods

```cmd
>>> len(deck)
```

當執行 `len(deck)` 時，`__len__` 會被 invoke

**<8>** 說明

一樣是 special methods

```cmd
>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[24]
Card(rank='K', suit='diamonds')
>>> deck[-1]
Card(rank='A', suit='hearts')
>>> deck[12::13]
[Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds')...]
```

當執行以上 code 時，`__getitem__` 會被 invoke，

先知道這樣用即可，未來會再做更詳細的介紹，因為是 slice 讓這功能如此強大:smile:

## 執行環境

* Python 3.6.4

## Reference

* [fluentpython/example-code](https://github.com/fluentpython/example-code)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)
