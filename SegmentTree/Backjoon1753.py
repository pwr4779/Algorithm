import sys

input = sys.stdin.readline()
l = []
tree = [0] * 3000000

#세그먼트 트리 생성
def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2)+init(node*2+1,(start+end)//2+1, end)
        return tree[node]

#구간 합 구하기
#node가 담당하는 구간[start, end]
#합을 구해야하는 구간 [left, right]

def subSum(node, start, end, left, right) :
    #겹치지 않는다면?? 합을 구해야하는 구간이 node가 담당하는 구간의 왼쪽이거나 오른쪽이면
    if left > end or right < start:
        return 0
    # 합의 범위는 [left, right]보다 [start, end]가 작으면?
    if left <= start and end >= right :
        return tree[node]

    # 조금이라도 겹치면 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색 시작
    return subSum(node*2, start, (start+end)//2, left,right) + subSum(node*2+1, (start+end)//2+1, left, right)

def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    #리프 노드가 아닌 경우에는 자식도 변경해줘야한다.
    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)

n, m, k = map(int, input.rstrip().split())

for _ in range(n):
    l.append(int(input.rstrip())) ##배열을 입력

init(1, 0, n-1)

for _ in range(m+k) :
    a, b, c = map(int, (input.rstrip().split()))

    if a == 1:
        b = b-1
        diff = c -l[b]
        l[b] = c
        update(1,0,n-1,b,diff)
    elif a==2:
        print(subSum(1,0,n-1,b-1,c-1))