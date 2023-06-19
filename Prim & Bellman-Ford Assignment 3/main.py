import assignment_3
import math

def main():                                                     #main function calling Prim's and Bellman-Ford's algorithms.
    graph = assignment_3.GraphTemplate()

    nodeA = assignment_3.NodeTemplate("A")
    nodeB = assignment_3.NodeTemplate("B")
    nodeC = assignment_3.NodeTemplate("C")
    nodeD = assignment_3.NodeTemplate("D")
    nodeE = assignment_3.NodeTemplate("E")

    nodeA.addConnection(nodeB, 2)
    nodeA.addConnection(nodeC, 3)
    nodeB.addConnection(nodeC, 4)
    nodeB.addConnection(nodeD, 5)
    nodeB.addConnection(nodeE, 1)
    nodeC.addConnection(nodeE, 6)
    nodeD.addConnection(nodeE, 3)

    graph.addNode(nodeA)
    graph.addNode(nodeB)
    graph.addNode(nodeC)
    graph.addNode(nodeD)
    graph.addNode(nodeE)

    assignment_3.printGraph(graph)
    print()

    print("Prim's Algorithm:")
    graph.primMST(nodeA)
    print()

    print("Bellman-Ford Algorithm:")
    graph.bellmanFord(nodeA)


if __name__ == "__main__":
    main()