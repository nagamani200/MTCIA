def count_digit(s):
    n_digit=0
    for i in s:
        #print("i=",i)
        if i in '0123456789':
            n_digit+=1
            #print("i:",i,"temp_vowel:",temp_vowel)
    return n_digit
str1=input()
a=count_digit(str1)
print(" no of digit in:' ",str1," 'is",a)
