class A:
    def __init__(self, array):
        self._list = array

    # def __len__(self):
    #     return len(self._list)


def length(obj):
    return len(obj._list)


A.__len__ = length

a = A([1, 2, 3])
print('length:', len(a))
