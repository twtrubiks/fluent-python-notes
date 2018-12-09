# What is the closures in python

[Youtube Tutorial - What is the closures in python](https://youtu.be/XxHg4fHDCmk)

這篇文章主要會介紹 closures，會使用 fluent python 中的範例來介紹，

以下是 fluent python 中對 closures 的解釋，

```text
a closure is a function that retains the bindings of the free variables that
exist when the function is defined, so that they can be used later when the
function is invoked and the defining scope is no longer available.
```

closure ( 閉包 ) 是一種函數，它保留定義函數時存在的 free variables ( 自由變數 ) 的綁定，

以便之後在調用函數並且定義 scope ( 範圍 ) 不再可用時可以使用它們。

以上看翻譯看不懂沒關係，我們來看例子:smile:

[demo1.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_closures/demo1.py)

```python
def make_average():
    # take advantage of the fact that series(lists) are ""mutable""
    series = []

    def average(new_value):
        # series is a free variable
        series.append(new_value)
        print('series', series)
        total = sum(series)
        return total / len(series)

    return average


avg = make_average()
print(avg(10))  # series [10]
print(avg(11))  # series [10, 11]
print(avg(12))  # series [10, 11, 12]

print(avg.__code__.co_freevars)  # ('series',)
```

當呼叫 `make_average()` 時，他會回傳 `average`(`average`為 inner function )，

而當 `average` 被呼叫，就會將參數傳入，並且添加到 `series` 中，最後計算目前的平均。

`series` 是 `make_average()` 中的 local variable，因為初始化 `series = []`

發生在這個 function 中，但是當 return average 時，他的 local scope 就消失了。

![img](https://i.imgur.com/m4lMALN.png)

free variable 的意思是指 `series` 不會被綁定在 local scope 中。

剛剛上面我們有特別強調 `series` 是 **mutable**，假如今天我們換上一個 **immutable**

會發生什麼事情呢:question:

[demo2.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_closures/demo2.py)

```python
def make_average():
    # count is a number or any immutable type
    count = 0
    total = 0

    def average(new_value):
        count += 1
        total += new_value
        return total / count

    return average


avg = make_average()
print('avg(10)', avg(10))

```

執行後，你會發現得到如下的錯誤，

```text
UnboundLocalError: local variable 'count' referenced before assignment
```

原因是因為在這邊我們是真的 assign 值給 count，使他變成一個 local variable，

( 而 count 根本還沒有定義，所以當然導致錯誤 )

而在 [demo1.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_closures/demo1.py) 中會正常 work，原因是我們只是使用 `series.append` ( 並沒有 assign 值給 series

，而是 method call )。

那如果我們真的想用 **immutable**，有什麼方法可以解決呢 :question:

在 python3 中提供了 `nonlocal` 給我們使用，可以將一個變數變成 free variable ( 即使是被 assign 一個新的值 )，

這邊要注意的是 `nonlocal` 不是 local variables，也不是 global variables，通常會使用在 nested function 中。

[demo3.py](https://github.com/twtrubiks/fluent-python-notes/blob/master/what_is_the_closures/demo3.py)

```python
def make_average():
    count = 0
    total = 0

    def average(new_value):
        # the nonlocal declaration was introduced in Python 3.
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return average


avg = make_average()
print('avg(10)', avg(10))
print('avg(11)', avg(11))
print('avg(12)', avg(12))

print(avg.__code__.co_freevars)  # ('count', 'total')
```

加上 `nonlocal` 之後，就可以正常 work 了。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
