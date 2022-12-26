def extract_consonant(s):
    temp_consonant=''
    for i in s:
        print("i=",i)
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            temp_consonant+=i
            print("i:",i,"temp_consonant:",temp_consonant)
    return temp_consonant
str1=input()
a=extract_consonant(str1)
print("consonant:",a)
