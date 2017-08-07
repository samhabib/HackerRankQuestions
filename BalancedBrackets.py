'''
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a
closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {},
and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is
not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single,
unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is considered to be balanced if the following conditions are met:

    It contains no unmatched brackets.
    The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair
    of brackets.

Given strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, print YES
on a new line; otherwise, print NO on a new line.

Input Format

The first line contains a single integer, , denoting the number of strings.
Each line of the subsequent lines consists of a single string, , denoting a sequence of brackets.

Constraints

    , where is the length of the sequence.
    Each character in the sequence will be a bracket (i.e., {, }, (, ), [, and ]).

Output Format

For each string, print whether or not the string of brackets is balanced on a new line. If the brackets are balanced,
 print YES; otherwise, print NO.

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output

YES
NO
YES


'''


'''
My Approach:
Well we knew that we had to keep track of all the open parenthesis, brackets, and squigglies in whatever order they came
 in from so it we had to think if we needed a stack or a queue. We needed a stack here because we needed to use a FIFO 
 method with comparing the open and close of the brackets. We then just run through the string and append all of the 
 open brackets we come across and if we reach any closed ones, then we just pop off the top of the stack and compare to
 see if they are matching. If they are great keep going till you reach the end of your string, if not return false. Also
 at the end you have to do one more check to see if the stack is empty that way we don't have any unclosed brackets in 
 the end.
 '''



def is_matched(expression):
    stack = []
    for char in expression:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
        elif char == ']' or char == ')' or char == '}':
            if stack:
                temp = stack.pop()
                if char == ')' and temp == '(':
                    pass
                elif char == ']' and temp == '[':
                    pass
                elif char == '}' and temp == '{':
                    pass
                else:
                    return False
            else:
                return False
    if stack:
        return False
    else:
        return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")