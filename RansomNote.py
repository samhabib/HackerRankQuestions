'''
A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.
Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

Input Format

The first line contains two space-separated integers describing the respective values of (the number of words in the magazine) and (the number of words in the ransom note).
The second line contains space-separated strings denoting the words present in the magazine.
The third line contains space-separated strings denoting the words present in the ransom note.

Constraints

    .
    Each word consists of English alphabetic letters (i.e., to and to ).
    The words in the note and magazine are case-sensitive.

Output Format

Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.

'''

'''
My Approach: Just simple Counter manipulation again and taking advantage of its unique methods. We subtract the magazine
counter from the ransom and if it leaves us with an empty counter we know that magazine has all the words we are looking
for in counter

'''


from collections import Counter


def ransom_note(magazine, ransom):
    ran = Counter(ransom)
    mag = Counter(mag)
    return ran - mag == {}


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
