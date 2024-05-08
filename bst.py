#!/usr/bin/python3
""" Module for BST class """
from base_tree import BinaryTreeBase


class BST(BinaryTreeBase):
    """ class for binary search tree
        insert => O(log(n))
        remove => o(log(n))
        search => o(log(n))
    """

    def insert(self, value):
        """ insert in BST """
        if self.data is None:
            self.data = value
            return self
        self.__insert(self, value)
        return self.search(value)

    @staticmethod
    def __insert(root, value):
        if not root:
            return BST(None, value)

        if value > root.data:
            root.right = root.__insert(root.right, value)
            root.right.parent = root
        elif value < root.data:
            root.left = root.__insert(root.left, value)
            root.left.parent = root

        return root

    @staticmethod
    def array_to_bst(arr):
        """ convert array to BST """
        if not arr or len(arr) == 0:
            return None
        tree = BST()

        for i in arr:
            tree.insert(i)

        return tree

    def search(self, value):
        """ search in BST """
        tmp = self
        while tmp:
            if tmp.data == value:
                return tmp
            elif value > tmp.data:
                tmp = tmp.right
            else:
                tmp = tmp.left
        return None

    def remove(self, value):
        """ remove from BST """
        return self.__remove(self, value)

    @staticmethod
    def __remove(root, value):
        """ remove value from BST """
        if not root:
            return None

        if value > root.data:
            print('remoe.right')
            root.right = root.__remove(root.right, value)
        elif value < root.data:
            root.left = root.__remove(root.left, value)
        else:
            """
                x
                  \
                   y
                    \
                     z <= remove
            """
            """
                x
                  \
                   y <= remove
                    \
                     z
                x
               /
              y <= remove
             /
            z
            """
            """
                x
                  \
                   y <= remove
                 /  \
               p     z
            """
            if not root.left and not root.right:
                print('how1')
                del root
                root = None
            elif not root.left:
                print('tmp')
                print('->root', root)
                tmp = root
                print('root', root)
                print('->root.right', root.right)
                root = root.right
                print('root.parent', root.parent)
                print('->tmp.parent', tmp.parent)
                root.parent = tmp.parent
                del tmp
            elif not root.right:
                print('how2')
                tmp = root
                root = root.left
                root.parent = tmp.parent
                del tmp
            else:
                print('how3')
                tmp = root.min_node(root.right)
                root.data = tmp.data
                root.right = root.__remove(root.right, tmp.data)
        return root

    @staticmethod
    def min_node(root):
        """ find min node for root """
        tmp = root
        while tmp.left:
            tmp = tmp.left
        return tmp
