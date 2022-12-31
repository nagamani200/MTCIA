fo=open(r"D:\pythonpractice38\day10\gaana.txt"+,"+w")
for i in range(5):
    inpstr=input("enter string:")
    fo.write(inpstr+'\n')
fo.close()
print("written to file")
