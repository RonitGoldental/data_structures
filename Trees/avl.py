from Trees.binary_search_tree_recursive import Bst
from math import fabs


class AvlNode:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
        self.height = 0


class Avl(Bst):

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if node is None:
            print("inserted ",data)
            return AvlNode(data)
        if data < node.data:
            node.left = self.insert_node(data, node.left)
        elif data > node.data:
            node.right = self.insert_node(data, node.right)
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        return self.settleViolation(data, node)

    def right_rotation(self, node):
        print("Rotating to the right on node ", node.data)
        temp_left = node.left
        node.left = temp_left.right
        temp_left.right = node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        temp_left.height = max(self.calc_height(temp_left.left), self.calc_height(temp_left.right)) + 1
        return temp_left

    def left_rotation(self, node):
        print("Rotating to the left on node ", node.data)
        tempright = node.right
        node.right = tempright.left
        tempright.left = node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        tempright.height = max(self.calc_height(tempright.left), self.calc_height(tempright.right)) + 1
        return tempright

    def calc_height(self, node):
        if not node:
            return -1
        return node.height

    def calc_balance(self, node):
        if not node:
            return -1
        return self.calc_height(node.left) - self.calc_height(node.right)

    def settleViolation(self, data, node):
        balance = self.calc_balance(node)
        # this is the Case I !!!! left-left heavy situation
        if balance > 1 and data < node.left.data:
            return self.right_rotation(node)
        # this is the Case II right-right !!!!
        if balance < -1 and data > node.right.data:
            return self.left_rotation(node)
        # left-right situation
        if balance > 1 and data > node.left.data:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        # right-left situation
        if balance < -1 and data < node.right.data:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node

    def remove_from_tree(self, value):
        if self.root:
            print("removing node", value)
            self.root = self.remove_node(value, self.root)

    def remove_node(self, value, node):
        if not node:
            return node
        if value < node.data:
            node.left = self.remove_node(value, node.left)
        elif value > node.data:
            node.right = self.remove_node(value, node.right)
        else:
            if node.right is None and node.left is None:
                del node
                return None
            elif node.right is None and node.left:
                temp_node = node.left
                del node
                return temp_node
            elif node.right and node.left is None:
                temp_node = node.right
                del node
                return temp_node
            else:
                predecessor = self.get_max_rec(node.left)
                node.data = predecessor.data
                node.left = self.remove_node(predecessor.data, node.left)
        if node is None:
            return node
        node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
        balance = self.calc_balance(node)
        # this is the Case I !!!! left-left heavy situation
        if balance > 1 and self.calc_balance(node.left) > 0:
            return self.right_rotation(node)
        # this is the Case II right-right !!!!
        if balance < -1 and self.calc_balance(node.right) < 0:
            return self.left_rotation(node)
        # left-right situation
        if balance > 1 and self.calc_balance(node.left) < 0:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        # right-left situation
        if balance < -1 and self.calc_balance(node.right) > 0:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node


avl = Avl()
for i in range(1,13):
    avl.insert(i)
avl.remove_from_tree(10)
avl.remove_from_tree(4)
avl.remove_from_tree(8)
avl.in_order_traversal()
print('end')

