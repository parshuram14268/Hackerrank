from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
shoe=dict(Counter(arr))
t=int(input())
money=0
for i in range(t):
    a,b=map(int,input().split())
    if a in shoe and shoe[a] >0:
        shoe[a]-=1
        money+=b
print(money)
