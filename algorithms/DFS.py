class Node:
    def __init__(self, data):
        self.data = data
        self.adjacentList = []
        self.visited = False


class DepthFirstSearch: #todo implement
    def dfs_iter(self, startNode):
        stack = [startNode]
        startNode.visited = True
        while stack:
            actualNode = stack.pop()
            print(actualNode.data)
            for vertex in actualNode.adjacentList:
                if not vertex.visited:
                    stack.append(vertex)
                    node.visited = True


    def dfs_rec(self, node):
        print(node.data)
        node.visited = True
        for vertex in node.adjacentList:
            if not vertex.visited:
                self.dfs_rec(vertex)

node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)
dfs = DepthFirstSearch()
# dfs.dfs_rec(node1)
dfs.dfs_iter(node1)