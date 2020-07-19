def solution(n, computers):
    vertex = [i for i in range(n)]
    graphset = []
    count = 0
    for start in range(n):
        visitedlist = []
        queue = [start]
        while queue:
            current = queue.pop()
            if not current in visitedlist:
                visitedlist.append(current)
                for j in range(n):
                    if computers[current][j]==1 and not j in visitedlist:
                        queue.insert(0,j)
        temp = graphset+visitedlist
        if len(set(temp)) != len(set(graphset)):
            count+=1
        graphset=temp
    return count

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n,computers))