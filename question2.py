"""
UMass ECE 241 - Advanced Programming
Homework #3   - Fall 2024
question2.py  - Binary Search Tree
"""
from tree_node import TreeNode

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # put the key and value in the tree
    def put(self, key, val):
        if self.root: # if root exists, call _put
            self._put(key, val, self.root) # put the key and value in the tree
        else:
            self.root = TreeNode(key, val) # if root does not exist, create a new node with key and value

    # put the key and value in the tree
    def _put(self, key, val, node):
        if key < node.key: # at current node if key is less than current node's key -> go left
            if node.hasLeftChild():
                self._put(key, val, node.leftChild) # go left until left child is None
            else:
                node.leftChild = TreeNode(key, val, parent=node) # if left child is None, create a new node
        else:
            if node.hasRightChild(): # same as above but for right child
                self._put(key, val, node.rightChild)
            else:
                node.rightChild = TreeNode(key, val, parent=node)

    def __setitem__(self, k, v):
        self.put(k, v)

    # get the node with the key from the tree
    def get(self, key):
        res = self._get(key, self.root) # get the node with the key from the tree
        if res is None: # if node is None, return None
            return None
        return res # return the node

    # get the node with the key from the tree
    def _get(self, key, node):
        if node is None: # if node is None, return None
            return None
        if node.key == key: # if key is found, return the node
            return node
        if key < node.key: # if key is less than current node's key -> go left
            return self._get(key, node.leftChild) # go left until left child is None
        else:
            return self._get(key, node.rightChild) # if key is greater than current node's key -> go right

    def __getitem__(self, key):
        return self.get(key)


    def find_path(self, element_1_key, element_2_key):
        """TODO: Fill in this function to get a path from element_1 to element_2"""
        src = self.get(element_1_key) # get the node with element_1_key
        dst = self.get(element_2_key) # get the node with element_2_key

        if not src or not dst: # if either of the nodes is None, return empty list
            return []

        # find the lowest common ancestor
        def find_lca(node, n1, n2):
            if not node:
                return None
            if node.key > n1 and node.key > n2:
                return find_lca(node.leftChild, n1, n2)
            if node.key < n1 and node.key < n2:
                return find_lca(node.rightChild, n1, n2)
            return node

        lca = find_lca(self.root, element_1_key, element_2_key)

        if not lca:
            return []

        # find the path from node to the node
        def find_path_to_node(node, key):
            path = []
            while node:
                path = [node] + path
                if node.key == key:
                    break
                if node.key > key:
                    node = node.leftChild
                else:
                    node = node.rightChild
            return path

        path1 = find_path_to_node(lca, element_1_key) # find the path from lca to element_1
        path2 = find_path_to_node(lca, element_2_key) # reverse the path2 and remove the first element

        return path1 + path2[::-1][1:]


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
