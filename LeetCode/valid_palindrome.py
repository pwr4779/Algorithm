

#list solution

def valid_check_palindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop(): # list pop() - Big O(n)
            return False
    return True

str_input = "A man, a plan, a canal: Panama"
print(valid_check_palindrome(str_input))

#deque optimizer
import collections
from typing import Deque

def isPalindrome(s: str) -> bool:
    strs: Deque = collections.deque() #deque

    for char in s:
        if char.isalnum():  #Is it alphabet or number
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  #deque's left pop : popleft() - Big O(1)
            return False

    return True

str_input = "A man, a plan, a canal: Panama"
print(isPalindrome(str_input))

#best solution
import regex as re
def isPalindrome(s: str) -> bool:
    s = s.lower()
    s= re.sub('[^a-z0-9]','',s) #regex
    return s == s[::-1] #slicing

str_input = "A man, a plan, a canal: Panama"
print(isPalindrome(str_input))

#reverse pythonic way
reverse_str =[]
reverse_str = str_input[::-1]
print(reverse_str)
reverse_str =[]
reverse_str[:] = str_input[::-1]
print(''.join(reverse_str))