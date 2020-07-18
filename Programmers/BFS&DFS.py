
#cycle check
def has_duplicates(seq):
    return len(seq) != len(set(seq))

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    queue = [start]

    #bfs
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                queue.insert(0, neighbor)
        visitedList.append(current)
    return visitedList

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedList = []

    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[edge[0]].append(edge[1])

    stack = [start]

    #dfs
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedList:
                stack.append(neighbor)
        visitedList.append(current)
    return visitedList


vertexList = [0, 1, 2, 3, 4, 5, 6]
#cycle example
#edgeList = [(0,1), (1,0), (0,2), (2,0),(1,3),(3,1),(2,4),(4,2),(2,5),(5,2),(4,6),(6,4),(4,5),(5,4)]

edgeList = [(0,1), (1,0), (0,2), (2,0),(1,3),(3,1),(2,4),(4,2),(2,5),(5,2),(4,6),(6,4)]
graphs = (vertexList, edgeList)
print(graphs)
print(bfs(graphs,0))
print(dfs(graphs,0))




