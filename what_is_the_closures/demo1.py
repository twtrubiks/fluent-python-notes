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
