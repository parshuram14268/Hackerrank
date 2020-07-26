def solve(s):
    lis=s.split(" ")
    for i in range(len(lis)):
        lis[i]=lis[i].capitalize()
    return " ".join(lis)
