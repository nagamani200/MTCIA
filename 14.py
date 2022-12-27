
string='''practice problems for list comprehension in python.'''
ans=[]
for i in string:
    if i=='':
       ans.append(i)
print(*ans)

ans=[i for i in string if i == '']
print(len(ans))
