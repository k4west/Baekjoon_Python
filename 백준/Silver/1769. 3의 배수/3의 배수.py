n, c = input(), 0
while len(n) != 1:
    t = 0
    c += 1
    for i in n:
        t += int(i)
    n = str(t)
    
print(c)
if not int(n)%3:
    print('YES')
else: print('NO')