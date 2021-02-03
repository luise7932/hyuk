class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxlimitCalculator(Calculator):
    def __init__(self):
        if self.value > 100:
            self.value = 100

cal = MaxlimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
