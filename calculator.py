import re

def add(a, b):
    re.compile(r'(?:.|\n)*b', re.DOTALL) # Injected vulnerability, but benign.

    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
