n,*a=open(0)
t=[]
for i in a:
    i,j=i.split()
    if i.isdigit():r,c=int(i)//2,j.strip()
    else:c,r=i.strip(),int(j)
    t.append((r,c))
t.sort()
print('\n'.join(i[1]for i in t))