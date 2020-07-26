from collections import defaultdict
a,m=map(int,input().split())
dic=defaultdict(list)
for i in range(a):
    dic[input()].append(i+1)
for i in range(m):
    x=input()
    if x in dic:
        for j in dic[x]:
            print(j,end=" ")
        print()
    else:
        print(-1)
