"""The exercise template contains a class named Person and a skeleton implementation for the class 
BabyCentre. A BabyCentre object performs various actions on a Person object. It may, for example, 
weigh or feed the person. In this exercise you will implement the rest of the BabyCentre class. 
Please do not change the class definition of Person in any way."""

class Person:
    def __init__(self, name: str, age: int, height: int, weigh: int):
        self.name = name 
        self.age = age
        self.height = height
        self.weigh = weigh

"""The BabyCentre class definition contains an outline for the function weigh. The method takes a Person 
object as its argument. It should return the weight of the person. 
You can access the weight of a person through the appropriate attribute defined in the Person class. 
Please fill in the rest of the implementation for the method weigh."""

class BabyCentre:
    def __init__(self):
        self.weigh_ins_count = 0

    """Please implement the method weigh_ins() which returns the total number of weigh-ins a BabyCentre 
    object has performed. NB: you will need a new attribute for keeping track of the number of weigh-ins."""

    def weigh_ins(self):
        return self.weigh_ins_count

    def weigh(self, person: Person):
        self.weigh_ins_count += 1
        # return the weight of the person passed as an argument
        return person.weigh

    """It is possible to change the state of an object passed as an argument. Please implement the method 
    feed(person: Person) which increases by one the weight of the person passed as an argument."""

    def feed(self, person: Person):
        person.weigh += 1

"""Below is an example of a main function where a BabyCentre weighs two separate Person objects:"""

baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

"""In the following example two persons are weighed, and then one of them is fed three times. 
Then the persons are weighed again:"""

baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")
print() 

baby_centre.feed(eric)
baby_centre.feed(eric)
baby_centre.feed(eric)

print(f"{eric.name} weighs {baby_centre.weigh(eric)} kg")
print(f"{peter.name} weighs {baby_centre.weigh(peter)} kg")

"""The printout should reveal that Eric's weight has increased by three."""

"""Code to test the method:"""

baby_centre = BabyCentre()

eric = Person("Eric", 1, 110, 7)
peter = Person("Peter", 33, 176, 85)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)
baby_centre.weigh(eric)

print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")