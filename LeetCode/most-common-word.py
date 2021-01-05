import regex as re
from collections import Counter
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub('[^\w]',' ',paragraph.lower()).split()
         if word not in banned]
counts = Counter(words)
print(counts)
first_common = counts.most_common(1)[0][0]
print(first_common)