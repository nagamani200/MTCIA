def printMonth(dn):
    mn=''
    if(dn==1):
       mn= "january"
    elif(dn==2):
       mn= "feb"
    elif(dn==3):
       mn= "march"
    elif(dn==12):
       mn= "december"
    else:
       mn="invalid"
    return mn






def printMonth1(dn):
    mn=''
    if(dn==1):
       mn= "january"
    if(dn==2):
       mn= "feb"
    if(dn==3):
       mn= "march"
    if(dn==12):
       mn= "december"
    
    return mn
import time
for i in range(3):
    inpNum=int(input())
    start=time.time()
    print(printMonth(inpNum))
    print(time.time()-start)
    start=time.time()
    print(printMonth1(inpNum))
    print(time.time()-start)
