"""The method tick adds one second to the stopwatch. The maximum value for both seconds and minutes is 59. 
Your class definition should also contain a __str__ method, which returns a string representation of the 
state of the stopwatch, as shown in the example above."""

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0


    def tick(self):
        if self.minutes == 59 and self.seconds == 59:
            self.seconds = 0
            self.minutes = 0
        elif self.seconds == 59:
            self.seconds = 0
            self.minutes += 1
        else:
            self.seconds += 1

    def __str__(self):
        minutes = str(self.minutes).zfill(2)
        seconds = str(self.seconds).zfill(2)
        return f"{minutes}:{seconds}"
        

watch = Stopwatch()
for i in range(3600):
    print(watch)
    watch.tick()