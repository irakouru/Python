# 1
'''In this exercise we'll practice forming conditional statements. That is,
statementswith a truth value. These are often used in if -statements and later
on as conditions in loops. In this exercise however, you won't need to worry
about any of that. Just form the conditions.
Write a statement that assigns to variable x the truth value depending on the
following condition:
a) x is true, if the value of variable y is a vowel.
b) x is true, if integer y is divisible by 7.
c) x is always falsed) x is true, if sum of variables a and b is either less
than 20 or greater than 50'''

# a)
y = input('Give a letter: ').lower() #We change every letter to small so that the program does not think that e.g. 'A' is not a vowel
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö']
if y in vowel_list:
    x= True
    print(x)
#if y == 'a' or y =='e'or y =='i' or y =='o' or y =='u' or y =='y' or y =='ä' or y =='ö':
    #x = True
    #print(x)
#elif y == 'A' or y == 'E' or y == 'I' or y =='O' or y =='U' or y =='Y' or y =='Ä' or y =='Ö':
    #x = True
    #print(x)
else:
    x = False
    print(x)

# b)
try:
    y = float(input('Give a number: '))
    x = None
    if y % 7 == 0: #Modulo from the given number must be 0 that the number is divided by 7
        x = True
        print (x)
    else:
        x = False
        print(x)
except:
    print('You must give a number.')

# c) 
x = False
if x == False:
    pass

else:
    pass

print(x)
#How Lasse did this:
if True: #if True is always True (checks if True is True), if you put "if False:" it checks if False is True > always False
    x = False   
    
# d)
x = None
a = int(input('Give a number: '))
b = int(input('Give a second number: '))
summa = a + b
if summa < 20 or summa > 50:
    x = True
    print(x)
else:
    x= False
    print (x)

# 2
'''Write a program that asks the user for a number of points gained from
solving programming exercises and outputs the grade according to the
following chart:
Points
Grade90-100: 5
80-89: 4
70-79: 3
60-69: 2
50-59: 1
0-50: Failed
If the user gives a number of points that is not on the chart, the program
outputs an error message about invalid input.'''

points = int(input('Enter the amount of exercise points: '))
if points < 50:
    print(f'With {points} points your grade is: Failed')
elif points >=50 and points < 60:                           #if points in range(50, 59):
    print(f'With {points} points your grade is: 1')
elif points >=60 and points < 70:                           # elif 60 <= points < 70:
    print(f'With {points} points your grade is: 2')
elif points >=70 and points < 80:
    print(f'With {points} points your grade is: 3')
elif points >=80 and points < 90:
    print(f'With {points} points your grade is: 4')
elif points >=90 and points <= 100:
    print(f'With {points} points your grade is: 5')
else:
    print(f'Points value out of range. Invalid input: {points}')

# 3
'''In this exercise we'll introduce the idea of a"guard" in conditional
statements. The purpose of these guards is to protect the program from
unexpected behavior. The idea isto form the conditional statements in such a
way that in statements with "and" -operator the first operand is evaluated
to False if we would run into division-by-zero situation with the second
operand. Here we'll benefit from the fact that if Python interpreter
identifies the first operand as false, the second operand is never evaluated.

"Guard" is a term used for a couple of different meanings. The idea is that
we'll be able to escape an unsafe situation as soon as possible. We'll return
to these when discussingfunctions.
a) Given the following program, modify the if statement in such a way that
you won't runinto division by zero problems. Use the logical 'and' -operator
to safeguard the insecure condition:

sum_of_numbers = int(input("Sum: "))
number_count = int(input("Number count: "))
if (sum_of_numbers / number_count) >= 100:
    print("Average number's value is >= 100.")
else:
    print("Average number's value is < 100.")
    
b)Are you able to change the previous program in such a way that you can use
logical 'or'-operator to safeguard the if statement? if so, how?'''

# a)
sum_of_numbers = int(input("Sum: "))
number_count = int(input("Number count: "))
if number_count != 0 and (sum_of_numbers / number_count) >= 100: #number_count cannot be 0
    print("Average number's value is >= 100.")
elif number_count == 0:
    print('Sum cannot be divided by 0')
else:
    print("Average number's value is < 100.")

# b)
'''sum_of_numbers = int(input("Sum: "))
number_count = int(input("Number count: "))
if (sum_of_numbers / number_count) >= 100 or (sum_of_numbers / number_count) < 100:
    if (sum_of_numbers / number_count) >= 100:
        print("Average number's value is >= 100.")
    else:
        print("Average number's value is < 100.")
else:
    print('Sum cannot be divided by 0')'''

#I think one cannot make this by using or-operator.

# 4
'''Given three numbers x, y and z. Sort the numbers without using the
built-in sort() or sorted() functions. That is, use if statements and
assignments to sort the three numbers. Then print them on screen in
ascending order. At the end of the program, you should have variables
"greatest", "middle" and "least" with the corresponding values stored in
them.'''
x = int(input('Give a number 1: '))
y = int(input('Give a number 2: '))
z = int(input('Give a number 3: '))
if x < y < z:
    least = x
    middle = y
    greatest = z
elif x < z < y:
    least = x
    middle = z
    greatest = y
elif y < x < z:
    least = y
    middle = x
    greatest = z
elif z < x < y:
    least = z
    middle = x
    greatest = y
elif z < y < x:
    least = z
    middle = y
    greatest = x
elif y < z < x:
    least = y
    middle = z
    greatest = x
print (f'{least}, {middle}, {greatest}')

