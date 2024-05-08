#!/usr/bin/python3
""" Base class for binary tree """


class BinaryTreeBase:

    def __init__(self, parent=None, data=None):
        """ Constructor for BinaryTreeBase """
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None

    def __str__(self):
        return "{}".format(self.data)

    def insert_left(self, data):
        """ insert a node as the left-child of another node """
        # Create new node with given parent and data
        if self:
            new_node = BinaryTreeBase(self, data)

        # insert the new node
        # if it already have left child replace it
        if self.left:
            new_node.left = self.left
            self.left.parent = new_node
        self.left = new_node

    def insert_right(self, data):
        """ insert a node as the right-child of another node """
        # Create new node with given parent and data
        if self:
            new_node = BinaryTreeBase(self, data)

        # insert the new node
        # if it already have left child replace it
        if self.right:
            new_node.right = self.right
            self.left.parent = new_node
        self.right = new_node

    def delete(self):
        """ Delete node from tree """
        # delete if node exist
        if not self:
            return

        # Delete left child
        self.delete(self.left)
        # Delete right child
        self.delete(self.right)
        # Delete current
        del self

    def is_leaf(self):
        """ Check if node is leaf node """
        if not self:
            return False
        if not self.left and not self.right:
            return True
        return False

    def is_root(self):
        """ Check if node is root """
        if self or not self.parent:
            return True
        return False

    def pre_order(self, func=None):
        """ Goes through binary tree using pre-order traversal """
        if not self or not func:
            return

        func(self.data)
        if self.left:
            self.left.in_order(func)
        if self.right:
            self.right.in_order(func)

    def in_order(self, func=None):
        """ Goes through binary tree using pre-order traversal """
        if not self or not func:
            return

        if self.left:
            self.left.in_order(func)
        func(self.data)
        if self.right:
            self.right.in_order(func)

    def post_order(self, func=None):
        """ Goes through binary tree using pre-order traversal """
        if not self or not func:
            return

        if self.left:
            self.left.in_order(func)
        if self.right:
            self.right.in_order(func)
        func(self.data)

    def height(self):
        """ Get height of a binary tree node """
        if not self:
            return 0
        hleft = self.left.height() + 1 if self.left else 0
        hright = self.right.height() + 1 if self.right else 0

        return hleft if hleft > hright else hright

    def depth(self):
        """ Get depth of a binary tree node """
        depth = 0

        if not self:
            return 0

        tmp = self
        while tmp.parent:
            depth += 1
            tmp = tmp.parent

        return depth

    def size(self):
        """ Get size of a binary tree """
        if not self:
            return 0

        left_size = self.left.size()
        right_size = self.right.size()
        size = left_size + right_size + 1

        return size

    def count_leaves(self):
        """ Count leaves in tree """
        if not self:
            return 0

        if not self.left and not self.right:
            return 1

        left_count = self.left.count_leaves()
        right_count = self.right.count_leaves()

        return left_count + right_count

    def nodes(self):
        """ Count nodes with at least 1 child in a binary tree """
        if not self:
            return 0

        if not self.left and not self.right:
            return 0

        nodes = 1 if self.left or self.right else 0
        nodes += self.left.nodes()
        nodes += self.right.nodes()

        return nodes

    def balance(self):
        """ Get the balance factor of a binary tree """
        if not self:
            return 0
        return self.left.height() - self.right.height()

    def is_full(self):
        """
        Check if binary tree is a full binary tree 
                    6
                  {   }
                 3     5
                {  }  {  }
               2   4  4   7
                    6
                  {   }
                 3     5
                {  }
               2   4
        """
        if not self:
            return False

        if self.left and self.right:
            left = self.left.is_full()
            right = self.right.is_full()

            return True if left and right else False
        elif not self.left and not self.right:
            return True

        return False

    def is_perfect(self):
        """ Check if a binary tree is perfect
                    6
                  {   }
                 3     5
                {  }  {  }
               2   4  4   7

            perfect => nodes = 2^h - 1
        """
        if not self:
            return False

        if self.nodes() == 2**self.height() - 1:
            return True
        return False

    def sibling(self):
        """ find sibling of a node """
        if not self or not self.parent:
            return None

        return self.parent.left if self.parent.right is self\
            else self.parent.right

    def uncle(self):
        """ find uncle of a node """
        if not self.parent:
            return None
        return self.parent.sibling()

    def common_ancestor(self, node):
        """ find the lowest common ancestor of two nodes """
        if not self or not node:
            return None
        first = self
        while first:
            second = node
            while second:
                if first == second:
                    return first
                second = second.parent
            first = first.parent
        return None

    def level_order(self, func=None):
        """ level order traversal """
        queue = [self]

        while queue:
            node = queue.pop(0)

            if node:
                func(node)
                queue.append(node.left)
                queue.append(node.right)

    def is_complete(self):
        """ Check if a binary tree is complete
                    6
                  {   }
                 3     5
                {  }
               2   4
               => True
                    6
                  {   }
                 3     5
                {  }    }
               2   4     7
               => False
        """
        if not self:
            return False
        queue = [self]
        end = False

        while queue:
            node = queue.pop(0)
            if not node:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True

    def is_bst(self):
        """ Check if binary tree is a BST
        BST:
            1- Left subtree of a node contains only nodes
                with less values than node value
            2- Right subtree of a node contains only nodes
                with greater values than node value
            3- Left and right subtrees each must be a binary search tree
            4- No duplicates
                    6
                  {   }
                 3     8
                {  }
               2   5
               => True
                    6
                  {   }
                 3     8
                {  }  {
               2   5  4
               => False
        """
        if not self:
            return False

        return self.__is_bst_helper(self, None, None)

    @staticmethod
    def __is_bst_helper(root, max_node, min_node):
        """ check if binary tree is BST """
        if not root:
            return True

        if (max_node and root.data >= max_node.data)\
                or (min_node and root.data <= min_node.data):
            return False

        return root.__is_bst_helper(root.left, root, min_node) and\
            root.__is_bst_helper(root.right, max_node, root)
