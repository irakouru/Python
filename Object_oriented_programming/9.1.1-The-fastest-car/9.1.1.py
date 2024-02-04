"""Createe a class named Car which represents the features of a car through 
two attributes: make (str) and top_speed (int).

Please write a function named fastest_car(cars: list) which takes a list of Car objects as its argument.

The function should return the make of the fastest car. You may assume there will always be a single 
car with the highest top speed. Do not change the list given as an argument, or make any changes to 
the Car class definition."""

from typing import Any

class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

def fastest_car(cars: list):
    top_speed = 0
    top_make = ""
    for car in cars:
        if top_speed < car.top_speed:
            top_speed = car.top_speed
            top_make = car.make
        else:
            continue 
    return top_make   

if __name__ == "__main__":
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280)
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))