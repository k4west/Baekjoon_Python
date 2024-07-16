def dictance(A, B):
    d = a_i = b_i = 0
    a_n, b_n = len(A), len(B)
    while a_i < a_n and b_i < b_n:
        if (s_a:=A[a_i]) != (s_b:=B[b_i]):
            d += 1
            if s_a < s_b:
                b_i -= 1
            else:
                a_i -= 1
        a_i += 1
        b_i += 1
    return d + a_n - a_i + b_n - b_i

n,*a=open(0)
t = []
for i in range(int(n)):
    A, B = map(lambda x: sorted(x.strip()), a[2*i:2*i+2])
    t.append(f'Case #{i+1}: {dictance(A, B)}')
print('\n'.join(t))