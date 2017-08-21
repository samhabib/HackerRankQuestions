'''
Check out the resources on the page's right side to learn more about strings. The video tutorial is by Gayle Laakmann
 McDowell, author of the best-selling interview book Cracking the Coding Interview.

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of
 each other if the first string's letters can be rearranged to form the second string. In other words, both strings
 must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc
  and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number
 of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings, a and  b, that may or may not be of the same length, determine the minimum number of character
deletions required to make and anagrams. Any characters can be deleted from either of the strings.

This challenge is also available in the following translations:

    Chinese
    Russian

Input Format

The first line contains a single string, .
The second line contains a single string, .

Constraints

    It is guaranteed that and consist of lowercase English alphabetic letters (i.e., through ).

Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.
'''


'''
My Approach:
This problem is extremely easy in python due to the Counter import. We store each letter  in a Count for both string a 
and b. Then we subtract the difference between a and b and that will leave us with all of the excess letters we have 
left over and they will be positive if a has more of those letters or negative if b has more of those letters. Then we
iterate all of our remaining numbers with an absolute value and add all of them together with the sum function and 
thats it

'''


from collections import Counter


def number_needed(a, b):
    aCount = Counter(a)
    bCount = Counter(b)
    aCount.subtract(bCount)

    return sum(abs(i) for i in aCount.values())


a = input().strip()
b = input().strip()

print(number_needed(a, b))
