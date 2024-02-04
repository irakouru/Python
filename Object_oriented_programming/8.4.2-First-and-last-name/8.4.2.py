"""Please write a class named Person with a single attribute name, which is set with an argument 
given to the constructor.

Please also add two methods:

The method return_first_name should return the first name of the person, while the method 
return_last_name should return the last name of the person.

You may assume that the name passed to the constructor will contain exactly two name elements 
separated with a space character."""

class Person():
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self):
        name_splitted = self.name.split(" ")
        first_name = name_splitted[0]
        return first_name
    
    def return_last_name(self):
        name_splitted = self.name.split(" ")
        last_name = name_splitted[1]
        return last_name


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())