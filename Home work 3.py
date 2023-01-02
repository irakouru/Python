'''1. The program asks a word. Then the program prints first the stars and
then the word.The total number of characters should be 15. For example,
if you typed the word school, the program prints the line

*********school'''

word=input("Give a word: ")
padded_word=word.rjust(15, '*')
print(padded_word)


'''2. ‘Prince Edward, the Queen's youngest son, and his wife Countess Sophie
published a statement thanking Queen Elizabeth II for her years of service.’

The text above should be printed so that there are no commas and no ’s'''

string="Prince Edward, the Queen's youngest son, and his wife Countess Sophie published a statement thanking Queen Elizabeth II for her years of service."
string2=string.replace(",", "")
string3=string2.replace("'","")
print(string3)


'''3. Find the index of the second article ‘the’ from the following sentence
using a suitable string method.

’Turku is a city and former capital on the southwest coast of Finland at
the mouth of the Aura River’'''

string4='Turku is a city and former capital on the southwest coast of Finland at the mouth of the Aura River'
second_the=string4.find('the', string4.find('the')+1) #finds the second 'the' by finding the first the and adding 1 to the index
print(second_the)


'''4. The program asks a word. If, for example, the word ‘elephant’ is
written, the program prints a frame outside the text. The frame changes
according to the word.

************

* elephant *

************'''

word2=input("Write a word: ")
edges1=word2.center(len(word2)+2, ' ')      #adds spaces before and after the word
edges2=edges1.center(len(edges1)+2, '*')    #adds * before and after the word
lenght=len(edges2)                          #calculates the lenght of the word with spaces and *
print(lenght*'*' + '\n\n' + edges2 + '\n\n' + lenght*'*')

