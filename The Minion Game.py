def minion_game(string):
    arr=['A','E','I',"O","U"]
    kevin=0
    stuart=0
    l=len(string)
    for i in range(l):
        if string[i] in arr:
            kevin+=l-i
        else:
            stuart+=l-i
    if(stuart>kevin):
        print('Stuart',stuart)
    elif(stuart<kevin):
        print('Kevin',kevin)
    else:
        print('Draw')
