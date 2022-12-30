def printSeriesDecreasing(ch,n):
    assert isinstance(ch,str),'first argument should be string'
    assert isinstance(n,int),'second argument should be string'
    for i in range(n,0,-1):
        print(ch*i)
    return None

inpCh=input("Enter a character:")
inpNum=int(input("Enter a number:"))

print('-'*40)
try:
    printSeriesDecreasing(inpCh,inpNum)
except AssertionError as ob:
    print(ob)
