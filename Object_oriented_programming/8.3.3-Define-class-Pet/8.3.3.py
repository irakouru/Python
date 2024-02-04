"""Please define the class Pet. The class should include a constructor, which takes the initial 
values of the attributes name, species and year_of_birth as its arguments, in that specific order.

Please also write a function named new_pet(name: str, species: str, year_of_birth: int) outside 
the class definition. The function should create and return a new object of type Pet, as defined 
in the class Pet."""

class Pet():

    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

new_pet = Pet("Vertti", "Cat", 2022)

print(new_pet.name)
print(new_pet.species)
print(new_pet.year_of_birth)