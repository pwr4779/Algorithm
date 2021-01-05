
from typing import List
logs = ["dig1 8 1 5 1", "left1 art can", "dig2 3 6","let2 own kit dig", "let3 art zero"]

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    # 로그의 가장 앞부분 문자 식별자를 제외하고 나머지를 가지고 sort를 하고 그 이후에 동일하다면 식별자 순으로 한다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return  letters + digits

print(reorderLogFiles(logs))
