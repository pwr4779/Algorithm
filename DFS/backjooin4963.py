import sys
sys.setrecursionlimit(10**8)

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,1,-1,1,1,-1,-1]

def dfs(x, y):
   visit[y][x] = 1
   for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1<nx<w and -1<ny<h and visit[ny][nx] != 1 and graph[ny][nx] == 1:
            dfs(nx, ny)

while True:
    w, h = map(int,sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    visit = [[0]*w for _ in range(h)]

    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and graph[i][j]==1:
                dfs(j,i)
                cnt += 1
    print(cnt)