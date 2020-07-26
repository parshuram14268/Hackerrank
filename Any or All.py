# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=list(map(str,input().split()))
print(all([int(i)>0 for i in arr]) and any([j == j[::-1] for j in arr]))
