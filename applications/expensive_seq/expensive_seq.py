from hashtable import HashTableEntry, HashTable
# Your code here

# cache = {}
# def expensive_seq(x, y, z):
#     # Your code here
#     # x/y/x f-string will be the key
#     entry = (x, y, z)
#     # if the entry is not in the cache 
#     if entry not in cache:
#         # if x equals 0, then return y+z (instructions say that x will not be less than 0)
#         if x <= 0:
#             v = y + z
#             cache[entry] = v
#         # otherwise perform the recursive function
#         else:
#             v = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
#             cache[entry] = v
#         # Store the cache entry
#         # Return result
#         return cache[entry]
#     # Return result
#     return cache[entry]

ht = HashTable(8)

def expensive_seq(x, y, z):
    entry = (x, y, z)
    
    if ht.get(entry) is None:
        if x <= 0: 
            v = y + z
            ht.put(entry, v)
        else:
            v = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            ht.put(entry, v)
        return ht.get(entry)
    return ht.get(entry)


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
