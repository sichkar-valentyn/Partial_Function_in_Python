# Explaining partial function and how to use it
# Importing partial from functools
from functools import partial

# Assigning to x integer number in binary notation
x = int('1101', base=2)
print(x)  # Showing result in decimal notation

# Creating function int_2 with partial
int_2 = partial(int, base=2)
x = int_2('1101')
print(x)


# Another examples how to sort lists easier with partial
x = [
    ('Guido', 'van', 'Rossum'),
    ('Haskell', 'Curry'),
    ('John', 'Backus')
]

y = ['abc', 'cba', 'abb']

import operator as op

# Creating function to sort lists by last element
sort_by_last = partial(list.sort, key=op.itemgetter(-1))

print(x)  # Showing current list
sort_by_last(x)
print(x)  # Showing sorted list

sort_by_last(y)
print(y)
