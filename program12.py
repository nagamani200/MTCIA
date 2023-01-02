
def printpattern(g,n):
    assert(n>=0),'INVALID'
    for i in range(n+1):
        print(g*i)
g=input()
n=int(input())
try:
    printpattern(g,n)
except AssertionError as a:
    print(a)
