'''You have a string
s = ‘Python is a good language’
Use slices and + to construct the string ‘Python is a language’ from s.'''

s="Python is a good language"
sliced=s[0:11]+s[16:25]
print(sliced)

'''Use input function to ask ‘Type here a word’. Print so many stars 
as the word has characters.
For example, you wrote the word ‘leopard’ and your code prints *******'''

word=input("Type here a word ")
lenght_word=len(word)
print(lenght_word*"*")

'''Slice and indexing work with lists too. Apply input function to ask three floats
from the user. Add every word to a list using append function. This function
works so that if the name of the list is  lst, lst.append(10) adds 10 to the list lst.
Finally print a new list which contains two first words from lst.'''

#Without loop
lst=[]
number1=float(input("Give me a floating point number: ")) #better way to write these would be: lst.append(float(input("Give a floating number")))
number2=float(input("Give me a floating point number: ")) #because we use these numbers only once, so we don't we have to store them into a variable
number3=float(input("Give me a floating point number: "))
lst.append(number1)
lst.append(number2)
lst.append(number3)
print(lst[0:2])

'''
#With a while loop
lst=[]
while len(lst)<3: #Must be 3 instead of four because first time when it goes trough the len is 0, 2 time len is 1, and third time len is 2 and only on the 
    number=float(input("Give me a floating point number: "))
    lst.append(number)
print(lst[0:2])

#With a for loop
lst=[]
for i in range(3):
    lst.append(float(input(f'Number {i+1}: ')))
print(lst[0:2])
'''

'''Use a tuple to assign x = 3, y = 8 and z = 4. With the help of x, y and z 
write the code which prints the tuple (4, 3, 8, 15). 15 = 4+3+8.'''

tupl=(3, 8, 4)
x=tupl[0]
y=tupl[1]
z=tupl[2]
new_tupl=(z, x, y, x+y+z)
print(new_tupl)
