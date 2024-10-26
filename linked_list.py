class Node:
    def __init__(self, init_key, init_data):
        self.key = init_key
        self.data = init_data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def setNext(self, new_next):
        self.next = new_next

    def __str__(self):
        return "[Key:{},Data:{}]".format(self.key, self.data)

class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, key):
        # searches and returns node with corresponding key
        current = self.head
        found = False
        stop = False
        found_node = None
        while (current is not None) and not found and not stop:
            if current.key == key:
                found = True
                found_node = current
            else:
                if current.key > key:
                    stop = True
                else:
                    current = current.next

        return found_node

    def add(self, key, data):
        # adds a node with key and data to the list
        current = self.head
        previous = None
        stop = False
        while (current is not None) and not stop:
            if current.key > key:
                stop = True
            else:
                previous = current
                current = current.next

        temp = Node(key, data)

        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current:
            count = count + 1
            current = current.next

        return count

    def __str__(self):
        print_list=""
        current = self.head
        while current is not None:
            print_list += str(current)
            print_list += "->"
            current = current.next

        print_list +="None"

        return print_list
    