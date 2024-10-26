"""
UMass ECE 241   -   Advanced Programming
Homework #3     -   Fall 2024
question1.py    -   Hashing with ordered list chaining
"""

from linked_list import OrderedList, Node

class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.occupied_slots = 0
        self.slots = [None] * self.size

    def put(self, key, data):
        """
        TODO: fill this function to put key-data pair
        TODO: in self.slots as per the question description
        """
        pass

    def slot_size(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        return self.slots[hashvalue].size()

    def slot_content(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        return self.slots[hashvalue]

    def hashfunction(self, key, size):
        return key % size

    def get(self, key):
        hashvalue = self.hashfunction(key, len(self.slots))
        key_node = self.slots[hashvalue].search(key)
        return key_node

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


# use this function to test your code (by instantiating objects and printing them)
def main():
    h = HashTable(11)
    h[1] = "grass"
    h[12] = "mass"
    print(h[1]) # Excepted: [Key:1,Data:grass]
    h[2] = 14
    h[1] = 2
    print(h[1], h[2], h[12]) # Excepted [Key:1,Data:2] [Key:2,Data:14] [Key:12,Data:mass]
    print(h.slot_size(1)) # Excepted 2
    print(h.slot_content(1)) # Excepted [Key:1,Data:2]->[Key:12,Data:mass]->None


if __name__ == '__main__':
    main()
