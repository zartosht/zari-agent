from sys import argv
from pkg.calculator import Calculator

expression = argv[1]
calculator = Calculator()
result = calculator.evaluate(expression)
print(result)