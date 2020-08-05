class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.contents = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.size/self.capacity

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # increase capacity
        self.capacity = new_capacity 
        # Store the old table
        old_contents = [None] * self.capacity
        # increase capacity and include the old table
        self.contents = self.contents + old_contents
        # re-hash all entries in the contents list 
        for i in range(0,self.capacity):
            current_entry = self.contents[i]
            # If the value of the current entry is None, then I don't need to do anything
            if current_entry is None:
                continue
            # otherwise I need to create a current linked-list variable for traversal
            else:
                linked_list_entry = self.contents[i]
            # While there is a current linked-list variable, I need to dedete it and re-hash it by running the "put" method on that variable's key and value
            while linked_list_entry:
                self.delete(self.contents[i].key)
                self.put(linked_list_entry.key, linked_list_entry.value)
                linked_list_entry = linked_list_entry.next


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash = 0xcbf29ce484222325
        for k in key:
            hash *= 0x100000001b3
            hash = hash ^ k
            # print(f"k: {k}, key: {key}, hash = {hash}, k-type: {type(k)}, key-type: {type(key)}")

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381 # "5831" seems to be an arbitrary number that works great for this. 
        # length_of_key = len(key)
        for i, k in enumerate(key):
            hash = (hash * 33) + ord(k)
            # hash = (hash * 33) + k
            print(f"k: {k}, key: {key}, hash = {hash}")
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # Find the index of the key
        entry_index = self.hash_index(key)
        current_entry = self.contents[entry_index]
        # Check to see if there is already an entry at that key (we'll know if there isn't because it will be "None"). And if there isn't, then I just create a new entry as the head, increment the size, and set its "next" pointer to be "None"
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)

        if self.contents[entry_index] is None:
            new_entry = HashTableEntry(key, value)
            self.contents[entry_index] = new_entry
            self.size += 1
        # Otherwise, there is an entry there and I need to determine if the key is already in the linked list or not, which is where the while-loop comes in
        while current_entry:
            # While iterating through the list, if I come across a node that is the same as the key, then I need to update that node's value
            if current_entry.key == key:
                current_entry.value = value
            # continue itterating through the list
            old_head = current_entry
            new_entry = HashTableEntry(key, value)
            self.contents[entry_index] = new_entry
            new_entry.next = old_head
            # Otherwise create a new entry with the key/value input as the new head
            self.size += 1
            current_entry = current_entry.next
 
    def get(self, key):
        """    
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # Keep track of the entries index as well as the current node I'm looking at 
        entry_index = self.hash_index(key)
        current_entry = self.contents[entry_index]
        # print(current_entry.value, ';aosidjf;oijao;sdjf')
        # Edge case: If there is nothing in this hash table, then return None
        if self.size == 0:
            return None
        # If the current entry is None, then just return "None" (because there is nothing there, so I don't need to continue iterating)
        if current_entry is None:
            return None
        # while there is a current entry, check to see if the key matches the key entered. If it does, then return that, otherwise increment the current entry
        while current_entry:
            if current_entry.key == key:
                return current_entry.value
            current_entry = current_entry.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Find the index of the key, and keep track of the current node
        entry_index = self.hash_index(key)
        # If the value at this index is None, then there is nothing to delete. So exit the function
        current_entry = self.contents[entry_index]
        

        if current_entry is None:
            return f"there is no entry there"
        # If head of the linked list is this key, then update the value to be where the current head's "next" is pointing towards
        if current_entry.key == key:
            self.contents[entry_index] = self.contents[entry_index].next
            self.size -= 1
            return key
        # Otherwise I need to iterate over the linked list to see if the entry is in there
        else:
            previous_entry = None
            while current_entry:
                if current_entry.key == key:
                    previous_entry.next = current_entry.next
                    self.size -= 1
                    return key
                previous_entry = current_entry
                current_entry = current_entry.next
                
        if (self.get_load_factor() < 0.2) and (self.capacity > MIN_CAPACITY):
            self.resize(self.capacity//2)






if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
