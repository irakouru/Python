class Dog:
    #A simple attempt to model a dog.

    def __init__(self, name, age, color):
        #Initialize name and age attributes.
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        #Simulate a dog sitting in response to a command.
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        #Simulate rolling over in response to a command.
        print(f"{self.name} rolled over!")

    def lay_down(self):
        #Simulate a dog laying down in response to command.
        print(f"{self.name} is now laying down.")



new_dog = Dog("Neppi", 12, "Grey")

print(new_dog.name)
new_dog.lay_down()

