'''"Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9"
'''
n=str(input("Enter a string value"))
a=b=0
for i in n:
    if i.isupper():
        i+=1
    elif i.islower():
        b+=1
    else:
        pass
print(a)
print(b)





