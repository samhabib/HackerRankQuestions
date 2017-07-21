def array_left_rotation(a, n, k):
    temp = n % k
    answer = [0] * n
    for x in range(0,n ):
        
        if x - temp < 0:
            answer[x] = a[(x-temp)+n]
            
        else:
            answer[x] = a[(x-temp)]
    return answer
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
