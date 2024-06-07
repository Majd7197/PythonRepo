class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

# Create an instance
md = MathDojo()

# Test the methods
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5

# Additional tests
y = md.add(10).add(3, 4).subtract(2, 1).result
print(y)  # should print 19

z = md.subtract(10).add(5).subtract(1, 1).result
print(z)  # should print 12
