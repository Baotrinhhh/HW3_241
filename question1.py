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
        hashvalue = self.hashfunction(key, len(self.slots)) # compute the hashvalue of the key

        if not self.slots[hashvalue]: # there is no collision
            self.slots[hashvalue] = OrderedList() # create a linked list at the slot at hashvalue
            self.slots[hashvalue].add(key, data) # add the key-data pair to the linked list
            self.occupied_slots += 1 # increment the number of occupied slots
        else:
            tmp = self.slots[hashvalue].search(key) # search for the key in the linked list of the slot at hashvalue
            if not tmp: # if the key is not found in the linked list
                self.slots[hashvalue].add(key, data) # add the key-data pair to the linked list
            else:
                tmp.setData(data) # if the key is found, update the data of the key

    def slot_size(self, key):
        hashvalue = self.hashfunction(key, len(self.slots)) # get the size of the linked list of the slot at hashvalue
        return self.slots[hashvalue].size()

    def slot_content(self, key):
        hashvalue = self.hashfunction(key, len(self.slots)) # get the linked list of the slot at hashvalue
        return self.slots[hashvalue]

    def hashfunction(self, key, size):
        return key % size # hashing function using modulo operator

    def get(self, key):
        hashvalue = self.hashfunction(key, len(self.slots)) # get the hashvalue of the key
        key_node = self.slots[hashvalue].search(key) # search for the key in the linked list of the slot at hashvalue
        return key_node

    def __getitem__(self, key):
        return self.get(key) # get the data of the key

    def __setitem__(self, key, data):
        self.put(key, data) # put the key-data pair


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
