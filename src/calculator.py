class FibonacciCalculator(object):
    def calculate(self, index):
        if index < 2:
            return index
        return self.calculate(index - 1) + self.calculate(index-2)
