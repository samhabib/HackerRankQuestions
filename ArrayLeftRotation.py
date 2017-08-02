'''A left rotation operation on an array of size shifts each of the array's elements unit to the left. For example,
if left rotations are performed on array , then the array would become .

Given an array of integers and a number, , perform left rotations on the array. Then print the updated
array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of (the number of
integers) and (the number of left rotations you must perform).
The second line contains space-separated integers describing the respective elements of the array's initial state.

Constraints

Output Format

Print a single line of space-separated integers denoting the final state of the array after performing
 left rotations.'''


'''
My Approach:
It doesn't matter how much high the number of rotations is to solve this problem, what matters is how high it is 
compared to the number of slots in our array because it will loop again and again if our number of of rotations is 
significantly greater than our number of integers. To solve this I took the # of Rotations and used a mod versus the
# of integers in our array which gave us how many left rotations we would have to actually do. Then to finish it the 
only challenge is that if we try to replace a number by subtracting the index we will eventually get to negative numbers
so all we have to do is add n to it to restart it at the beginning (in this case the end of the array since its a left 
rotation)
'''

def array_left_rotation(a, n, k):
    temp = k % n
    answer = [0] * n
    for x in range(0, n):

        if x - temp < 0:
            answer[x - temp + n] = a[x]

        else:
            answer[x - temp] = a[x]

    return answer


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')