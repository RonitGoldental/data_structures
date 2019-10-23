class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert_start(self, value):
        self.size += 1
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
        else:
            newnode.next = self.root
            self.root = newnode

    # o(1)
    def size3(self):
        return self.size

    # o(N)
    def size2(self):
        size = 0
        node=self.root
        while node is not None:
            node = node.next
            size+=1
        return size

    #o(N)
    def insert_end(self, value):
        self.size += 1
        newnode = Node(value)
        iter_node = self.root
        while iter_node.next is not None:
            iter_node = iter_node.next
        iter_node.next = newnode

    def traverslist(self):
        iter_node = self.root
        while iter_node is not None:
            print(iter_node.value)
            iter_node=iter_node.next

    def remove(self,value):
        iter_node = self.root
        prev_node = None
        while iter_node is not None:
            if iter_node == self.root:
                if iter_node.value == value:
                    self.root == iter_node.next
                    del iter_node
                    self.size -=1
                    break
                else:
                    prev_node=iter_node
                    iter_node = iter_node.next
            else:
                if iter_node.value == value:
                    prev_node.next = iter_node.next
                    del iter_node
                    self.size -= 1
                    break
                else:
                    iter_node = iter_node.next
                    prev_node = prev_node.next



linkedlist= LinkedList()
linkedlist.insert_start(12)
linkedlist.insert_start(122)
linkedlist.insert_start(3)
linkedlist.insert_end(31)
linkedlist.traverslist()
print(linkedlist.size3())
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)
print(linkedlist.size3())

