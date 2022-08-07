# What is the Descriptor in python

這篇文章主要會介紹 Descriptor (描述器)

建議先對 [What is the property](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_property) 有一定的認識:smile:

除了可以用 property 限制設定的值之外, 也可以使用今天要介紹的 Descriptor.

```python
class DataDescriptor:

    """a.k.a. data descriptor or enforced descriptor"""

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value

            # error
            # leading to infinite recursion.
            # setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must > 0")


class A:
    data = DataDescriptor("data")

    def __init__(self, data):
        self.data = data


a = A(123)
print(a.data)
a1 = A(-1) # ValueError: value must > 0
```

透過 DataDescriptor 可以攔截 instance 屬性的 get 和 set,

( 當 Descriptor 成為 某class 的 屬性成員時,

可攔截該 class 的 instance 屬性中的 `__get__` `__set__` `__delete__` )

在這邊 `__set__` 不能使用 `setattr(instance, self.storage_name, value)`

原因是因為 `data = DataDescriptor("data")` 名稱都是 data, 會導致 infinite recursion.

如果你想要使用 `setattr(instance, self.storage_name, value)`, 需將名稱改變.

修改如下,

```python
class DataDescriptorV2:

    """a.k.a. data descriptor or enforced descriptor"""

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must > 0")


class A:
    data = DataDescriptorV2("data1")

    def __init__(self, data):
        self.data = data


a = A(123)
print(a.data)
a1 = A(-1) # ValueError: value must > 0
```

既然相同的名稱會導致錯誤, 這樣嘗試讓他自動填入 attribute name,

修改如下,

```python
class DataDescriptorV3:
    __counter = 0

    """a.k.a. data descriptor or enforced descriptor"""

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = "_{}#{}".format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError("value must > 0")


class A:
    data = DataDescriptorV3()

    def __init__(self, data):
        self.data = data


a = A(123)
print(a.data)
# a1 = A(-1)  # ValueError: value must > 0
```

透過 `__counter`, 自動將 `storage_name` 命名為 `_DataDescriptorV3#0`.

也可以使用 Descriptor 實作 ReadOnly

(但如果只是要實作簡單的 readonly, 建議直接使用 property 比較方便簡單:smile:)

程式碼如下,

```python
class ReadOnlyDescriptor:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        return self.storage_name

    def __set__(self, instance, value):
        raise AttributeError("read-only attribute")


class A:

    data = ReadOnlyDescriptor("data")


a = A()
print(a.data)
a.data = 123  # AttributeError: read-only attribute
```

只需要實作 `__set__`, 並顯示合適的訊息.

如果只有 `__get__`, 沒有 `__set__`, 則是所謂的 NonData Descriptor.

```python
class NonDataDescriptor:

    """a.k.a. non-data or shadowable descriptor"""

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        return instance.__dict__[self.storage_name]
```

NonDataDescriptor 很適合使用在 cache 快取,

假設某個運算花費很大, 可以把它快取起來, 程式碼如下

```python
import time


class NonDataDescriptor:

    """a.k.a. non-data or shadowable descriptor"""

    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __get__(self, instance, owner):
        print("trigger __get__")
        time.sleep(5) # simulation expensive
        instance.__dict__[self.storage_name] = self.storage_name
        return self.storage_name


class A:

    data = NonDataDescriptor("data")


a = A()
print(a.data)
print(a.data)
print(a.data)
```

上面這段 code, 只會輸出一次 `trigger __get__`, 剩下都是直接透過快取取資料.


## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
