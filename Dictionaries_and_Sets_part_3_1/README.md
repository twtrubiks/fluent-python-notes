# Dictionaries and Sets - Part 3-1

[Youtube Tutorial - Dictionaries and Sets - Part 3-1]()

***Because of their crucial role, Python dicts are highly optimized. Hash tables are the engines behind Python’s high-performance dicts.***


```text
All mapping types in the standard library use the basic dict in their implementation,
so they share the limitation that the keys must be hashable (the values need not be
hashable, only the keys).
```

如果不認識 hashable

[Youtube Tutorial - What is the Hashable](https://youtu.be/-Qw3V2VoEQg)

[What is the Hashable](https://github.com/twtrubiks/fluent-python-notes/tree/master/what_is_the_hashable)

## Dictionaries 介紹

[dictionary_using_items.py](https://github.com/twtrubiks/python-notes/blob/master/dictionary_using_items.py) - dictionary.items()

[dictionary_get.py](https://github.com/twtrubiks/python-notes/blob/master/dictionary_get.py) - dictionary get()

[dictionary_update.py](https://github.com/twtrubiks/python-notes/blob/master/dictionary_update.py) - dictionary update()

[dict.fromkeys_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/dict.fromkeys_tutorial.py)

### dict Comprehensions

以下例子 dictcomps

```python
numbers = [1, 2, 3]
{number: number * 2 for number in numbers}
```

dictcomps 和 liscomps 是很相似的,

如果不了解 liscomps, 可參考[An Array of Sequences - Part 2-1](https://github.com/twtrubiks/fluent-python-notes/tree/master/A_Array_of_Sequences_part_2_1)

### Handling Missing Keys with setdefault

A subtle mapping method is setdefault. We don’t always need it, but when we do, it
provides a significant speedup by avoiding redundant key lookups.

[setdefault_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/setdefault_tutorial.py)

# Mappings with Flexible Key Lookup

Sometimes it is convenient to have mappings that return some made-up value when a missing key is searched.

有兩種方法

defaultdict , add  `__missing__` method

# defaultdict: Another Take on Missing Keys

先來介紹 defaultdict

[defaultdict_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/defaultdict_tutorial.py)

舉個例子, `dd = defaultdict(list)`

假如 `new-key` 沒有在 dd 中, 當執行 dd['new-key'] 步驟如下

1. 先呼叫 `list()` 建立一個新的 list

2. 將 new-key 插入 dd 中 (使用 new-key 當作 key)

3. 回傳 list

The callable that produces the default values is held in an instance attribute called default_factory.

Create a  defaultdict with the list constructor as default_factory.

If no default_factory is provided, the usual  KeyError is raised for missing keys.


The  default_factory  of a  defaultdict  is only invoked to pro‐
vide default values for  __getitem__  calls, and not for the other
methods. For example, if  dd  is a  defaultdict , and  k  is a missing key,  dd[k]  will call the  default_factory  to create a default value, but  dd.get(k)  still returns  None .

The mechanism that makes  defaultdict work by calling  default_factory is actually the __missing__ special method,


# The __missing__ Method

if you
subclass  dict and provide a  __missing__ method, the standard  dict.__getitem__ will
call it whenever a key is not found, instead of raising  KeyError.

```python
# Tests for item retrieval using `d[key]` notation::
>>> d = StrKeyDict0([('2', 'two'), ('4', 'four')])
>>> d['2']
'two'
>>> d[4]
'four'
>>> d[1]
Traceback (most recent call last):
    ...
KeyError: '1'

# Tests for item retrieval using `d.get(key)` notation::
>>> d.get('2')
'two'
>>> d.get(4)
'four'
>>> d.get(1, 'N/A')
'N/A'


# Tests for the `in` operator::
>>> 2 in d
True
>>> 1 in d
False
```

[eg_3_6.py](eg_3_6.py)

1. StrKeyDict0 inherits from dict.

2. Check whether key is already a str. If it is, and it’s missing, raise KeyError.

3. Build str from key and look it up.
4. The  get method delegates to  __getitem__ by using the  self[key] notation; that
gives the opportunity for our __missing__ to act.

5. If a  KeyError was raised,  __missing__ already failed, so we return the  default.

6. Search for unmodified key (the instance may contain non-str keys), then for a
str built from the key.