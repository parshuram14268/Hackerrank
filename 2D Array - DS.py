def hourglassSum(arr):
    r=len(arr)
    c=len(arr[0])
    s=-100
    for i in range(r-2):
        for j in range(c-2):
            top=arr[i][j]+arr[i][j+1]+arr[i][j+2]
            mid=arr[i+1][j+1]
            down=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if s<(top+mid+down):
                s=top+mid+down
    return s
