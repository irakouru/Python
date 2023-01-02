#1
'''a) Convert the string "15.5" into integers. Try to do this directly from
the given string first. Afterward convert the string first to a float and
then from float to an int. Explain why this happens.
b) Convert the boolean value True into string. Now convert the boolean value
first to integer andthen from integer to string.
c) Convert the floating point value 1.1 into integers. Convert the resulting
integer back into floatingpoints.d) Convert the string "Esther” into a list.
Convert that list back to a string. Print the string onscreen. Then print
the first index of that string on screen.
e) As a conclusion from a)-d), what can you say about invertibility of type
conversions?'''

#a)
string = "15.5"
#string_to_integers = int(string) Gives value error because 15.5 is float
#print(string_to_integers)
string_to_float = float(string)
float_to_integer = int(string_to_float)
print(float_to_integer)

#b)
boolean = True
boolean_to_string = str(boolean)
#print(boolean_to_string)
boolean_to_integer = int(boolean)
integer_to_string = str(boolean_to_integer)
print(integer_to_string)

#c)
floating_point_number = 1.1
floating_point_number_to_integer = int (floating_point_number)
integer_to_floating_point_number = float(floating_point_number_to_integer)
print(integer_to_floating_point_number)

#d)
string2 = "Esther"
string2_to_list = list(string2)
back_to_string = str(string2_to_list)
print(back_to_string)
print(back_to_string[0])

'''Conversions from one type to another and
back to the original type are not opposite to each other.'''

#2
'''2Implement a program that asks the user for three numbers. The program
calculates and prints the meanvalue and average absolute deviation of the
given numbers.
We'll be using the Python built-in function abs() here. abs() returns the
absolute value of a numbergiven as its parameter. So, for example
abs(-3) would return 3.
You can use the following formulas for thecalculations:Mean value of numbers
x1, x2 and x3:mean_value = (x1 + x2 + x3) / 3
Absolute deviation of number x1:abs_dev_x1 = abs(x1 - mean_value)
Average absolute deviation:avg_abs_dev = (abs_dev_x1 + abs_dev_x2 + abs_dev_x3) / 3'''

number1 = float(input('Give number 1: '))
number2 = float(input('Give number 2: '))
number3 = float(input('Give number 3: '))
mean = (number1 + number2 + number3)/3
abs_dev_number1 = round(abs(number1-mean), 1)
abs_dev_number2 = round(abs(number2-mean), 1)
abs_dev_number3 = round(abs(number3-mean), 1)
average_abs_dev = (abs_dev_number1 + abs_dev_number2 + abs_dev_number3)/3
print(f'Mean value: {mean}')
print(f'Absolute deviation of number 1: {abs_dev_number1}\nAbsolute deviation of number 2: {abs_dev_number2}\nAbsolute deviation of number 3: {abs_dev_number3}')
print(f'Average absolute deviation: {average_abs_dev}')

'''Program fails if I input something else than a float or integer, e.g. string,
because string is different data type and the calculations can't be performed'''

#3
'''Given a random floating point number num_a, form a floating point number
num_b such that its integerpart is num_a's fractional part and its fractional
part is num_a's integer part.'''

import random

num_a = round(random.uniform(0, 99.99),2)
num_a_string = str(num_a)
splitted = num_a_string.split(".")
first = splitted[1]
second = splitted [0]
new_number = first + "." + second
num_b = float(new_number)
print(num_b)

#4
'''Implement a program that asks the user for the number of enrolled students
on a course and themaximum amount of students per lab group. The program
then calculates the minimum number of labgroups that are needed to fulfil
the given constraints. Try to solve this without conditionalstatements (that
is, do not use "if" -statements which we have not discussed on lectures yet).'''

number_of_students = int(input("How many students have enrolled on the course? "))
maximum_for_group = int(input( "What's the maximum number of students per lab group? "))
number_of_groups = (number_of_students + maximum_for_group - 1)// maximum_for_group
print(f'The minimum number of lab groups needed with these constraints: {number_of_groups}')




      

                


                
                



