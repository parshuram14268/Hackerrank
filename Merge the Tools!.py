def merge_the_tools(string, k):
    l=len(string)
    div=l//k
    for i in range(0,l,k):
        x=string[i:k+i]
        arr=list(x)
        lis=[]
        for c in arr:
            if c not in lis:
                lis.append(c)
        print("".join(lis))
