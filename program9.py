sample_dict = {
    "name": "Gaanu",
    "age" : 22,
    "salary":50000,
    "city":"new york"
}

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)
