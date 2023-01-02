"""sample_dict ={
    "name":"Gaanavi",
    "age": 23,
    "salary":80000,
    "city": "Newyork"}
keys =["name","salary"]
newDict = { sample_dict[i] for i in keys }
print(newDict)"""



sample_dict ={
    "name":"Gaanavi",
    "age": 23,
    "salary":80000,
    "city": "Newyork"}
keys =["name","salary"]
newDict = {}
for i in keys:
    newDict[i]=sample_dict[i]
print(newDict)
