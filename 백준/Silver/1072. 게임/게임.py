X,Y=map(int,input().split())
print(bool((Z:=(Y*100)//X)>=99)*-1 or bool(int(i:=(X*(Z+1)-100*Y)/(99-Z))!=i)+int(i))