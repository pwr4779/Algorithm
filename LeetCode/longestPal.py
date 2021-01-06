
def logestPalindromel(s: str) -> str:
    #예외 처리
    if len(s)<2 or s==s[::-1]:
        return s
    result = ''
    for i in range(len(s)-1):
        #크기가 2인 윈도우와 크기가 3인 윈도우로 전진하면서 판단
        result = max(result, expand(s, i,i+1), expand(s, i,i+2), key=len)
    return result

def expand(s: str, left: int, right: int) -> str:
    while left>=0 and right<=len(s)-1 and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]#index 주의

strs = 'beabaed'

print(logestPalindromel(strs))