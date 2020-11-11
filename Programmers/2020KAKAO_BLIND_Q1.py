
def solution(s):
    if len(s)< 3:
        return len(s)

    min = len(s)
    for i in range(1, len(s)//2 + 1):
        start = i
        result = []
        prev =  s[0:i]
        count = 1
        while True:
            now = s[start:start+i]
            if now == prev:
                count +=1
            else:
                result.extend([str(count),prev])
                count = 1
                prev = now
            if start > len(s):
                break
            start += i
        result = ''.join(result)
        result=result.replace(str(1),'')
        print(result)
        if len(result) < min:
            min = len(result)
    answer = min
    return answer



print(solution('aabbaccc'))