"""Please define a new class named Clock which expands on the capabilities of your Stopwatch class. 
the constructor should take initial values for the hours, minutes and seconds as arguments, and set 
these appropriately. The tick method adds one second to the clock. The set method sets new values for 
the hours and the minutes, and sets the seconds to zero."""

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        if hours <= 23 and minutes <= 59 and seconds <= 59:
            self.seconds = seconds
            self.minutes = minutes
            self.hours = hours
        else: 
            print("The given values are incorrect.")


    def tick(self):
        if self.hours == 23 and self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
            self.hours = 0
        elif self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0 
            self.hours += 1
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1

    def set(self, hours: int, minutes:int):
        if hours <= 23 and minutes <= 59:
            self.hours = hours
            self.minutes = minutes
            self.seconds = 0
        else:
            print("Incorrect value given.")
        
    def __str__(self):
        hours = str(self.hours).zfill(2)
        minutes = str(self.minutes).zfill(2)
        seconds = str(self.seconds).zfill(2)
        return f"{hours}:{minutes}:{seconds}"
        

watch = Clock(22, 58, 50)
for i in range(360):
    print(watch)
    watch.tick()

watch.set(12, 22)
print(watch)
