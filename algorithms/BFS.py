class Node:
    def __init__(self, data):
        self.data = data
        self.adjacentList= []
        self.visited = False

class BreadthFirstSearch:
    def bfs(self,startNode):
        queue = [startNode]
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.data)
            for vertex in actualNode.adjacentList:
                if not vertex.visited:
                    queue.append(vertex)
                    vertex.visited = True
                    

node1= Node("a")
node2= Node("b")
node3= Node("c")
node4= Node("d")
node5= Node("e")
node1.adjacentList.append(node2)
node1.adjacentList.append(node3)
node2.adjacentList.append(node4)
node4.adjacentList.append(node5)
bfs= BreadthFirstSearch()
bfs.bfs(node1)


