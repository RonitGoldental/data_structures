class Node:

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None



class Bst:

    def __init__(self):
        self.root = None
# not recursive
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            iter_node = self.root
            while iter_node is not None:
                if data < iter_node.data:
                    if iter_node.left is None:
                        iter_node.left = Node(data)
                    else:
                        iter_node = iter_node.left
                elif data > iter_node.data:
                    if data > iter_node.data:
                        if iter_node.right is None:
                            iter_node.right = Node(data)
                    iter_node = iter_node.right
                else:
                    break


    def get_min(self):
        iter_node = self.root
        while iter_node.left is not None:
            iter_node = iter_node.left
        return iter_node.data


    def get_max(self):
        iter_node = self.root
        while iter_node.right is not None:
            iter_node = iter_node.right
        return iter_node.data

    def insert_rec(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            iter_node = self.root
            while iter_node is not None:
                if data < iter_node.data:
                    if iter_node.left is None:
                        iter_node.left = Node(data)
                    else:
                        iter_node = iter_node.left
                elif data > iter_node.data:
                    if data > iter_node.data:
                        if iter_node.right is None:
                            iter_node.right = Node(data)
                    iter_node = iter_node.right
                else:
                    break

    def remove_from_tree(self,value):
        pass




b = Bst()
b.insert(5)
b.insert(6)
b.insert(7)
b.insert(4)
b.insert(7)
b.insert(8)
print("the min is {}".format(b.get_min()))
print("the max is {}".format(b.get_max()))
print("rec- the min is ",b.get_min_rec())
print("rec- the max is ",b.get_max_rec())
#print(f'the max is {b.get_max()}')

