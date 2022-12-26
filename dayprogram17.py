def count_consonant(s):
    n_consonant=0
    for i in s:
        #print("i=",i)
        if i in 'BCDEFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            n_consonant+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return n_consonant
str1=input()
a=count_consonant(str1)
print(" no of consonant in:' ",str1," 'is",a)
