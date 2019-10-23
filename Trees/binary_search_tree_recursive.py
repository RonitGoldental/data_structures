class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


class Bst:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_node(data, node.left)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_node(data, node.right)

    def get_min(self):
        if self.root is not None:
            return self.get_min_rec(self.root)
        else:
            return None

    def get_min_rec(self, iter_node):
        if iter_node.left is None:
            return iter_node.data
        else:
            return self.get_min_rec(iter_node.left)

    def get_max(self):
        if self.root is not None:
            return self.get_max_rec(self.root).data
        else:
            return None

    def get_max_rec(self, iter_node):
        if iter_node.right is None:
            return iter_node
        else:
            return self.get_max_rec(iter_node.right)

    def in_order_traversal(self):
        if self.root is not None:
            self.in_order_traversal_rec(self.root)

    def in_order_traversal_rec(self, node):
        if node.left is not None:
            self.in_order_traversal_rec(node.left)
        if node is not None:
            print(node.data)
        if node.right is not None:
            self.in_order_traversal_rec(node.right)

    def remove_from_tree(self, value):
        if self.root:
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
            predesesor = self.get_max_rec(node.left)
            node.data = predesesor.data
            node.left = self.remove_node(predesesor.data, node.left)
        return node

    def height_root(self):
        if self.root:
           return self.node_height(self.root)
        return 0

    def node_height(self, node):
        if node is None:
            return -1
        return max(self.node_height(node.left), self.node_height(node.right))+1

if __name__ == "__main__":
    main()

def main():
    b = Bst()
    b.insert(5)
    b.insert(6)
    b.insert(7)
    b.insert(4)
    b.insert(7)
    b.insert(8)
    b.insert(14)
    b.insert(12)
    b.insert(15)
    print("the min is {}".format(b.get_min()))
    print("the max is {}".format(b.get_max()))
    b.in_order_traversal()
    b.remove_from_tree(15)
    b.in_order_traversal()
    b.remove_from_tree(5)
    b.in_order_traversal()
    print(b.height_root())
    # b.remove_from_tree(7)
    # b.in_order_traversal()
    # b.remove_from_tree(4)
    # b.in_order_traversal()
    # b.remove_from_tree(8)
    # b.in_order_traversal()
