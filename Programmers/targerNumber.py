import collections
from itertools import product

#완전탐색
def solution1(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

#dfs
def solution2(numbers, target):
    answer = 0
    queue = collections.deque([(0,0)])
    while queue:
        current_sum, num_idx = queue.popleft()
        if num_idx  == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            queue.append((current_sum - number, num_idx + 1))
            queue.append((current_sum + number, num_idx + 1))

    return answer

print(solution1([1,1,1,1,1], 3))
print(solution2([1,1,1,1,1], 3))