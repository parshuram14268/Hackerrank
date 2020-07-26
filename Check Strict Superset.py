arr=set(map(int,input().split()))
t=int(input())
status=True
for i in range(t):
    s=set(map(int,input().split()))
    status=status and s.intersection(arr) == s
print(status)
