# Insort keeps a sorted sequence always sorted
import bisect
import random

SIZE = 7
random.seed(1729)  # Initialize the random number generator.

my_list = []
for i in range(SIZE):

    # This is equivalent to choice(range(start, stop, step)), but doesn’t actually build a range object.
    new_item = random.randrange(SIZE * 2)

    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)
