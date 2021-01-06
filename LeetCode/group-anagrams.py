import collections
from typing import List
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strs: List[str])->List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(groupAnagrams(strs))
