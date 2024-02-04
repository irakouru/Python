"""The exercise template contains a partially completed class DecreasingCounter:

Please complete the method decrease defined in the template, so that it decreases the value stored in 
the counter by one. See the example above for expected behaviour.

Please add functionality to your decrease method, so that the value of the counter will never reach 
negative values. If the value of the counter is 0, it will not be further decreased.

Please add a method set_to_zero which sets the value of the counter to 0.

Please add a method reset_original_value() which resets the counter to its initial state."""

class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value > 0:
            self.value -= 1
        else:
            pass

    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.initial_value


counter = DecreasingCounter(10)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

counter = DecreasingCounter(2)
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()
counter.decrease()
counter.print_value()

counter = DecreasingCounter(100)
counter.print_value()
counter.set_to_zero()
counter.print_value()

counter = DecreasingCounter(55)
counter.decrease()
counter.decrease()
counter.decrease()
counter.decrease()
counter.print_value()
counter.reset_original_value()
counter.print_value()