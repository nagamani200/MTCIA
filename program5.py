"""employees = ['Gaanavi','Nagamani']
defaults ={"designation":'developer',"salary": 80000}

for i in employees:
    data[i]=defaults
print(data)"""



employees = ['Gaanavi','Nagamani']
defaults ={"designation":'developer',"salary": 80000}

data=dict.fromkeys(employees, defaults)
print(data)
