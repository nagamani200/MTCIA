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
for i in range(3):
    inpNum=int(input())
    print(printMonth(inpNum))
