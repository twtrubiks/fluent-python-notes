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
