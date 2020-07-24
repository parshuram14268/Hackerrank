def rotLeft(a, d):
    for i in range(d):
        temp=a.pop(0)
        a.append(temp)
    return a
   
# or another apporach
''''
