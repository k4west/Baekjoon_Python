n = 10**6
p = [False, False] + [True] * (n-1)
for i in range(2, int(n**.5)+1):
    if p[i]:
        for j in range(i*i, n+1, i):
            p[j] = False
ans = []
for i in map(int, open(0).readlines()[:-1]):
    j = i
    tmp = set()
    for k in range(2, i+1):
        if p[k]:
            while j%k == 0:
                j //= k
                tmp.add(k%10)
        if j == 1:
            break
    if tmp == {3}:
        ans.append(f'{i} YES')
    else:
        ans.append(f'{i} NO')
print('\n'.join(ans))