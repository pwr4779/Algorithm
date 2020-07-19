def solution(begin, target, words):
    if not target in words:
        return 0
    words.append(begin)
    n = len(words)
    edgelist = []
    for i in range(n):
        for j in range(n):
            if i != j:
                a = words[i]
                b = words[j]
                count =0
                for k in range(len(a)):
                    if a[k] != b[k]:
                        count+=1
                if count==1:
                    edgelist.append((i, j))
    answer = bfs(words, edgelist, target)
    return answer

def bfs(words, edgelist, target):
    adj = [[] for word in words]
    for edge in edgelist:
        adj[edge[0]].append(edge[1])

    queue = [(len(words) - 1,0)]
    visitedlist = []
    while queue:
        current = queue.pop()
        if words[current[0]] == target and current[1]<=len(words):
            return current[1]
        visitedlist.append(current[0])
        for next in adj[current[0]]:
            if not next in visitedlist:
                queue.insert(0, (next,current[1]+1))
    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))