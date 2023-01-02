sample_dict = {
    "name": "Gowthu",
    "age" : 22,
    "salary":50000,
    "city":"new york"
}
keys = ["name", "salary"]


for k in keys:
    sample_dict.pop(k)
print(sample_dict)



