#1
'''Some countries measure temperature in Fahrenheit degrees. The conversion
formula between Celsius and Fahrenheit scales is
c / 5 = (f -32) / 9
Your task is to design a code that asks three integer variables start, end
and step. The program prints a table where the first column contains the
degrees in Fahrenheit and the second column has degrees in Celsius. The rows
begin from start to end with increments step in Fahrenheit scale. In addition,
start and end are included.'''

start = int(input('Give a start degree in F: '))
end = int(input('Give an end degree in F: '))
step = int(input('Give a step degree in F: '))
f_and_c = []

for f in range(start, end+1, step):
        c = round(((f-32) /9) *5, 1)
        f_and_c.append((f, c))


for_print = '\n'.join(map(str, f_and_c))
for_print = str(for_print)
for_print = for_print.replace('(' , '')
for_print = for_print.replace(')' , '')
for_print = for_print.replace(',' , ' ')
lines = 10* '-'
print(f'F   C\n{lines}\n{str(for_print)}')

#2
'''Again we utilize randrange() function to roll a dice.
Task: Roll a dice until you will get 6. However, roll max 5 times.'''

import random
rolls = []
x = True
while x == True: 
    number = random.randrange(1, 7)
    rolls.append(number)

    if number != 6 and len(rolls) < 5:
        continue
    else:
        x = False
        '''rolls = str(rolls)
        rolls = rolls.replace(',', '')
        rolls = rolls.replace('[', '')
        rolls = rolls.replace(']', '')'''
        print ('Rolling:', *rolls)
        
#3
'''Retrieved from the currency exchange rates table
https://www.x-rates.com/table/?from=EUR&amount=1
Oct 09, 2022 08:58 UTC
we can see that
1 euro = 0.974015 US Dollar
1 euro = 0.878185 British Pound
1 euro = 6.929159 Chinese Yuan Renminbi
Write a program that asks first ‘How many euros?’and calculates and prints
the amount in three different currencies according to the table. The program
asks in the end: ‘Do you want to continue?’ You can answer ‘y’or ‘n’.
If your answer is ‘y’, the program goes to the beginning, and you can
continue as far as you want. The program ends when your answer is ‘n’. If
you answered something else, the message ‘You did not answer y or n’
is displayed and the program continues from the beginning.'''

while True:

        euro = float(input('How many euros? '))
        dollar = round(euro * 0.974015, 2)
        pound = round(euro * 0.878185, 2)
        yuan = round(euro * 6.929159, 2)

        print (f'{euro} € is {dollar} $\n{euro} € is {pound} £\n{euro} € is {yuan} ¥') 
        variable = input("Do you want to continue? You can answer 'y' or 'n'. ")
        if variable == 'y':
                continue
        elif variable == 'n':
                break
        else:
                print("You did not answer y or n")
                continue

#4
'''It is possible to pause the running program (so called thread) with the
function sleep() thatis inthe module named time. The pause can be n
(positive integer) seconds.
How do you code a program that asks the variable start (the positive integer)
and then counts down starting fromstart? The program prints the numbers from
start to one (including both). Each number is pausing at one second.
In this exercise while-loop is required'''

import time
start = int(input("Give a starting integer (positive): "))


for i in reversed(range(start+1)):      #+1 that also the asked number is iterated
        if i == 0:
                print("Boom!")
        else:
                print(i)
                time.sleep(1)           #Waits 1s before the execution is continued
        
        
