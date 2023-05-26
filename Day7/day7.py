# Write a Python program to combine two dictionary by adding values for common keys



def combine(d1,d2):
    return (d2.update(d1))



d1 = {'e': 100, 'f': 200, 'g':300}
d2 = {'a': 300, 'b': 200, 'd':400}


combine(d1,d2)

print(d2)


# Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.

import json


string  = '{"key1":"value1","key2":"value2","key3":"value3"}'


dict = json.loads(string)

print(dict)


#Write a Python program to sort Counter by value.

from collections import Counter
x = Counter({'Math':81, 'Physics':83, 'Chemistry':87})
x.most_common()
print(x)