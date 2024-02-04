"""Please write a class named NumberStats with the following methods:

-the method add_number adds a new number to the statistical record
-the method count_numbers returns the count of how many numbers have been added
-the method get_sum should return the sum of the numbers added (if no numbers have been added, 
the method should return 0)
-the method average should return the mean of the numbers added (if no numbers have been added, 
the method should return 0)

Please write a main program which keeps asking the user for integer numbers until the user types in -1. 
The program should then print out the sum and the mean of the numbers typed in.

Please add to your main program so that it also counts separately the sum of the even and the odd numbers added.

NB: do not change your NumberStats class definition in this part of exercise, either. Instead, define 
three NumberStats objects. One of them should keep track of all the numbers, another should track the 
even numbers, and the third should track the odd numbers typed in.

Your program should use a NumberStats object to keep a record of the numbers added.

At this point there is no need to store the numbers themselves in any data structure. 
It is enough to simply remember how many have been added. The add_number method does take an argument, 
but there is no need to process the actual value in any way just yet."""

class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0

    def add_number(self, number:int):
        self.numbers += number
        self.counter += 1

    def count_numbers(self):
        return self.counter
    
    def get_sum(self):
        if self.counter == 0:
            return 0
        else:
            return self.numbers
        
    def average(self):
        if self.counter == 0:
            return 0
        else:
            return self.numbers/self.counter

if __name__ == "__main__":    

    stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()

    while True:
        number = int(input("Enter a positive number (end by entering -1): "))
        if number >= 0:
            stats.add_number(number)
            if number % 2 == 0:
                even_stats.add_number(number)
            else:
                odd_stats.add_number(number)
        elif number == -1:
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            print("Sum of even numbers:", even_stats.get_sum())
            print("Sum of odd numbers:", odd_stats.get_sum())
            break
        else:
            print("Please enter a positive number!")
            continue

"""if __name__ == "__main__":        
    stats = NumberStats()

    while True:
        number = int(input("Enter a positive number (end by entering -1): "))
        if number >= 0:
            stats.add_number(number)
        elif number == -1:
            print("Sum of numbers:", stats.get_sum())
            print("Mean of numbers:", stats.average())
            break
        else:
            print("Please enter a positive number!")
            continue"""

"""stats.add_number(3)
stats.add_number(5)
stats.add_number(1)
stats.add_number(2)
print("Numbers added:", stats.count_numbers())"""
