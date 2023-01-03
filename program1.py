"""def printPattern(ch,n):
    sp='.'
    for i in range(0,n):
        print(sp*(n-i-1)+ch*(2*i+1)+sp*(n-i-1))
    return None
inpCh=input()
inpNum=int(input())
printPattern(inpCh,inpNum)"""

def printSeries(n):
    for i in range(1,n+1):
        num=1
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None
inpNum = int(input())
printSeries(inpNum)
