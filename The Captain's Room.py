# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
arr=list(map(int,input().split()))
family=len(arr)//k
s=set(arr)
print((k*sum(s)-sum(arr))//(k-1))

