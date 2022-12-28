#nums=[11,22,33,44,55]
#import math
#print(nums)
#result= list(map(math.sqrt,nums))
#print(result)


nums=[11,22,33,44,55]
import math
result=[math.sqrt(i) for i in nums]
result=[]
for i in nums:
    result.append(math.sqrt(i))
print(result)
