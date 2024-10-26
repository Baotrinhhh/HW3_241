"""
UMass ECE 241 - Advanced Programming
Homework #3   - Fall 2024
question2.py  - Binary Search Tree
"""
from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

    def _put(self, key, val, node):
        if key < node.key:
            if node.hasLeftChild():
                self._put(key, val, node.leftChild)
            else:
                node.leftChild = TreeNode(key, val, parent=node)
        else:
            if node.hasRightChild():
                self._put(key, val, node.rightChild)
            else:
                node.rightChild = TreeNode(key, val, parent=node)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        res = self._get(key, self.root)
        if res is None:
            return None
        return res

    def _get(self, key, node):
        if node is None:
            return None
        if node.key == key:
            return node
        if key < node.key:
            return self._get(key, node.leftChild)
        else:
            return self._get(key, node.rightChild)

    def __getitem__(self, key):
        return self.get(key)


    def find_path(self, element_1_key, element_2_key):
        """TODO: Fill in this function to get a path from element_1 to element_2"""
        pass



def main():
    mytree = BinarySearchTree()

    mytree[4] = "red"
    mytree[8] = "yellow"
    mytree[6] = "blue"
    mytree[3] = "pew"

    print(mytree[6])
    print(mytree[2])

    path = mytree.find_path(3, 8)

    for i, node in enumerate(path):
        print(node, end=' --> ' if i < len(path) - 1 else '')


if __name__ == "__main__":
    main()
