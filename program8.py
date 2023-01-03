set1 ={10,20,30}
set2 ={20,40,50}
if set1.isdisjoint(set2):
    print("Two sets have no items in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))
