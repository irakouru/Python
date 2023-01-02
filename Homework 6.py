#1
'''The tuples are like lists, but immutable. However, the tuples have other
advantages.
list_ = [1, 2, 3, 'a', 'b', 'c',True, 2.5]
tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)'''
#a)
''' Import the module sys and utilise the function getsizeof().
Look at Python documentation to see, what it is doing. Apply this function
to our list and tuple. What are your observations?'''

#Get sizeof() gives the size of a particular objectin bytes. Getsizeof()
#is a system specific method and need sys module to work. 

import sys

list_ = [1, 2, 3, 'a', 'b', 'c', True, 2.5]
tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)

print(sys.getsizeof(list_))
print(sys.getsizeof(tuple_))

#Tuples need less memory.

#b)
'''Import the module timeit. Here you use the timeit function timeit() to
see the running timeof the code.
For example, the code 2 ** 10 is run one million times.
timeit.timeit("2 ** 10")
0.010506924998480827# seconds
Check the running times creating the literal list like list_ and the running
time of the literal like tuple_. How do you compare list and tuple?'''
import timeit

print(timeit.timeit("2 ** 10"))

print(timeit.timeit("list_ = [1, 2, 3, 'a', 'b', 'c', True, 2.5]"))
print(timeit.timeit("tuple_ = (1, 2, 3, 'a', 'b', 'c', True, 2.5)"))

#Tuple is faster to create.

#c)
'''Manipulating with tuples
# name, age, country
item1 = ('Charlie Brown', 11, 'USA')
name = item1[0]
age = item1[1]
country = item1[2]
print(f'Name is {name}, age is {age}, country is {country}')
Name is Charlie Brown, age is 11, country is USA
How to derive name, age and country with unpacking of tuples?'''

# name, age, country
item1 = ('Charlie Brown', 11, 'USA')
name = item1[0]
age = item1[1]
country = item1[2]
print(f'Name is {name}, age is {age}, country is {country}')

#Unpacking of tuples:
item1 = ('Charlie Brown', 11, 'USA')
(name, age, country) = item1
print(f'Name is {name}, age is {age}, country is {country}')

#2
'''Here you should use list methods. Please check the table in the lecture
file named Lists.
a) The list li contains names.li = ['John', 'Liza', 'Peter', 'Mary']
To remove the last name from li you should find a correct method.
b) Add the name ‘Charlie’ between ‘Liza’ and ‘Peter’ using an appropriate
method.
c) String has a method join(). Explain, how to use it.Then apply join to
print all the names of li with each name on its own line.
d) Make a program that asks a small number n. The program prints stars with
n columns and n rows.'''

#a)
li = ['John', 'Liza', 'Peter', 'Mary']

#With pop-method:
#li.pop()
#print(li)

#With del:

del li[-1]
print(li)

#b)
li = ['John', 'Liza', 'Peter', 'Mary']

index_Liza = li.index('Liza')
li.insert(index_Liza + 1, 'Charlie')
print(li)

#c)
#The join() method takes all items in an iterable and joins them into
#one string.

li = ['John', 'Liza', 'Peter', 'Mary']
string = '\n'.join(li)
print(string)

#d)

number_of_stars = int(input('Give me a small number: '))
total = number_of_stars * [number_of_stars * '*']
output = '\n'.join(total)
print(output)

#3
'''This exercise uses functions of random module and ranges and lists.
list(range(1, 4)) returns [1, 2, 3]'''

#a)
'''Your program prints [2, 4, 6, 8, 9, 7, 5, 3, 1] using range and + operator.'''

lst = list(range(1, 10))
new_lst = [lst[1] , lst[3] , lst[5] , lst[7], lst[8] , lst [6] , lst[4] , lst[2] , lst[0]]
print(new_lst)

#b)
'''The code
import random
li = ['John', 'Liza', 'Peter', 'Mary']
should give a random word.'''

import random
li = ['John', 'Liza', 'Peter', 'Mary']
print(random.choice(li))

#c)
'''We roll a dice 12 times.rolls = random.choices(range(1, 7), k = 12)
How many 6’s are there?'''

import random
#lista = []
rolls = random.choices(range(1, 7), k=12)
#lista.append(rolls) Can't do like this because would be [[rolls]]?
occurrences_of_six = rolls.count(6)
print(f'The numbers are: {rolls}\nThe occurrences of sixes are {occurrences_of_six}')

#d)
'''The Finnish lottery takes 7 random integers between 1-40 (both included).
fin_lot = random.sample(range(1, 41), 7)
Sort the numbers from the smallest to the greatest.'''
import random
fin_lot = random.sample(range(1, 41), 7)
fin_lot.sort()
print(fin_lot)

#4
'''We have a deck of playing cards.'''

suits = ['♣', '♦', '♥', '♠']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(s, v) for s in suits for v in values]

#a)
'''Calculate the number of the cards of the deck.'''

number_of_cards = len(deck)
print(number_of_cards)

#b)
'''Change the suit of the second card ('♣', '3') to the card (‘♠’, '3').
What are your notions and why?'''

#second = deck.pop(1)
#second[0] = '♠'

#Values in a tuple cannot be replaced, tuples are immutable.

#c)
'''Shuffle the deck and take one random card and print it in the form e.g. ♣K'''

import random
random.shuffle(deck)
#print(deck)
one_card = random.choice(deck)
print(''.join(one_card))

#d)
'''Deal the cards for 4 players.'''

index = int(len(deck)/2)
print(index)

half_1 = deck[:index]
half_2 = deck[index:]

index_2 = int(len(half_1)/2)
index_3 = int(len(half_2)/2)

half_3 = half_1[:index_2]
half_4 = half_1[index_2:]

half_5 = half_2[:index_3]
half_6 = half_2[index_3:]

print(f'First player has the following cards: {half_3}')
print(f'Second player has the following cards: {half_4}')
print(f'Third player has the following cards: {half_5}')
print(f'Fourth player has the following cards: {half_6}')

#Better way:

cards_per_player = len(deck)//4
for player in range(4):
    player_cards = []
    for c in range(cards_per_player):
        r_card = random.choice(deck)
        deck.pop(deck.index(r_card))
        player_cards.append(r_card)

    print(f'Card for player {player+1} are {player_cards}')






