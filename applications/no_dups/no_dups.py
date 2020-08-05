from hashtable import HashTableEntry, HashTable


def no_dups(s):
    cache = {}
    # Your code here
    new_sentence = s.split()
    # print(s)
    for word in new_sentence:
        val = 0
        # print(word)
        if word.isspace():
            continue
        if word not in cache:
            cache[word] = val
        else:
            cache[word] += 1
    shortened_sentence = ' '.join(cache.keys())
    return shortened_sentence

            


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))