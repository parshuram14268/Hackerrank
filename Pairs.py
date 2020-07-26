def pairs(k, arr):
    s=set(arr)
    count=0
    for j in arr:
        dif= j-k
        if dif in s:
            count+=1
    return count
