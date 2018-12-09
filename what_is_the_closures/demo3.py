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
