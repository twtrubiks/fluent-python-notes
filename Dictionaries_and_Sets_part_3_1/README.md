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

