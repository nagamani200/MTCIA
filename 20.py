#string='''practice problems for List comprehension in python.'''
#ans=[]
#for i in string:
    #if i not in 'AEIOUaeiou':
        #ans.append(i)
        #print(*ans)
    
#print(*ans)

ans=[i for i in string if  i not in 'AEIOUaeiou']
print(*ans)
