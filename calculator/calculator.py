
def calculate(expression):
    try:
        return eval(expression)
    except (SyntaxError, TypeError):
        return "Invalid expression"
