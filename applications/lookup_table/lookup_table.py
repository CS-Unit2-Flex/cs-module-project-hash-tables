# Your code here
import math
import random
from hashtable import HashTableEntry, HashTable

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

# USING A TUPLE
# # Create a cache
# cache = {}
# def slowfun(x, y):
#     """
#     Rewrite slowfun_too_slow() in here so that the program produces the same
#     output, but completes quickly instead of taking ages to run.
#     """
#     # Your code here
#     entry = (x,y)
#     # If x/y isn't in the cache, then run the slow function and create a new entry
#     if entry not in cache: 
#         v = slowfun_too_slow(x, y)
#         cache[entry] = v
#     # Store x/y as key and output of above function as value
#         return cache[entry]
#     # Otherwise just return the value from the cache     
#     return cache[entry]


# USING AN F-STRING 
# Create a cache
# cache = {}
# def slowfun(x, y):
#     """
#     Rewrite slowfun_too_slow() in here so that the program produces the same
#     output, but completes quickly instead of taking ages to run.
#     """
#     # Your code here
#     entry = f"{x},{y}"
#     # If x/y isn't in the cache, then run the slow function and create a new entry
#     if entry not in cache: 
#         v = slowfun_too_slow(x, y)
#         cache[entry] = v
#     # Store x/y as key and output of above function as value
#         return cache[entry]
#     # Otherwise just return the value from the cache     
#     return cache[entry]


# USING MY HASHTABLE
ht = HashTable(8)

def slowfun(x, y):
    # entry = f"{x}, {y}"
    entry = (x, y)
    # print(entry, ';aoijsdf;oijao;sdfjio;asdijfo')

    if ht.get(entry) is None:
        v = slowfun_too_slow(x, y)
        ht.put(entry, v)
        return ht.get(entry)
    return ht.get(entry)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
    # print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')

