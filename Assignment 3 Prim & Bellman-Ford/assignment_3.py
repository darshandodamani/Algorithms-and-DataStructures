#Reference: Pseudocode from pdf and graphtemplate.
#Authors: Darshan Dodamani (124753), Prajwal Basavaraj Gaddigoudar(124729).
import math

class NodeTemplate:
    def __init__(self, label):
        self.label = label
        self.adjacentNodes = {}
        self.parent = None
        self.distance = math.inf

    def addConnection(self, node, weight):           #adding a connection
        self.adjacentNodes[node] = weight

    def removeConnection(self, node):                #removing a connection
        if node in self.adjacentNodes:
            del self.adjacentNodes[node]

    def setParent(self, parent):                     #manipulating parent
        self.parent = parent

    def setDistance(self, distance):                 #manipulating distance
        self.distance = distance


class GraphTemplate:
    def __init__(self):
        self.nodes = []

    def addNode(self, node):                         #adding a node
        self.nodes.append(node)

    def removeNode(self, node):                      #removing a node
        if node in self.nodes:
            self.nodes.remove(node)

    def printGraph(self):                            #prints the graph
        print("Graph:")
        for node in self.nodes:
            print(node.label)
            for neighbor, weight in node.adjacentNodes.items():
                print("->", neighbor.label, "=", weight)

    def primMST(self, start):                        #implementation of Prim's algorithm taking minheap as priority queue
        for node in self.nodes:
            node.setDistance(math.inf)
            node.setParent(None)

        start.setDistance(0)
        minHeap = MinHeap(self.nodes)
        minHeap.buildMinHeap()

        while minHeap.isNotEmpty():
            u = minHeap.extractMin()

            for v, weight in u.adjacentNodes.items():
                if minHeap.contains(v) and weight < v.distance:          #if v is not fully analysed than updates it's values
                    v.setParent(u)
                    v.setDistance(weight)
                    minHeap.decreaseKey(v)

        print("Minimum Spanning Tree:")
        for node in self.nodes:
            if node.parent:
                print(node.parent.label, "->", node.label, "=", node.distance)

    def bellmanFord(self, start):                      #implementation of Bellman Ford's algorithm
        for node in self.nodes:
            node.setDistance(math.inf)
            node.setParent(None)

        start.setDistance(0)

        for _ in range(len(self.nodes) - 1):           #checks nodes-1 times if every edge can be relaxed
            for u in self.nodes:
                for v, weight in u.adjacentNodes.items():
                    if u.distance != math.inf and u.distance + weight < v.distance:
                        v.setParent(u)
                        v.setDistance(u.distance + weight)

        for u in self.nodes:                           #checks for negative cycle
            for v, weight in u.adjacentNodes.items():
                if u.distance != math.inf and u.distance + weight < v.distance:
                    return False

        print("Shortest Paths:")
        for node in self.nodes:
            if node.distance != math.inf:
                print(start.label, "->", node.label, "=", node.distance)


class MinHeap:                                         #minheap class for priority queue selection 
    def __init__(self, nodes):
        self.heap = [(node.distance, node) for node in nodes]
        self.size = len(nodes)

    def buildMinHeap(self):                            #iterates over array of elements from middle element and calls minHeapify to each element 
        for i in range(self.size // 2 - 1, -1, -1):
            self.minHeapify(i)

    def minHeapify(self, i):                           #maintains the property of minheap by extracting the smallest element with a key value smaller than the current minimum
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        if right < self.size and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.minHeapify(smallest)

    def extractMin(self):                                     #extracting an element from minheap
        if self.size == 0:
            return None

        minNode = self.heap[0][1]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.minHeapify(0)

        return minNode

    def decreaseKey(self, node):                             # updating the key values of nodes in a binary min heap
        for i in range(self.size):
            if self.heap[i][1] == node:
                self.heap[i] = (node.distance, node)
                break

        parent = (i - 1) // 2

        while i > 0 and self.heap[parent][0] > self.heap[i][0]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def isNotEmpty(self):
        return self.size > 0

    def contains(self, node):
        for i in range(self.size):
            if self.heap[i][1] == node:
                return True
        return False


def printGraph(graph):                                          #prints the graph
    print("Graph:")
    for node in graph.nodes:
        print(node.label)
        for neighbor, weight in node.adjacentNodes.items():
            print("->", neighbor.label, "=", weight)