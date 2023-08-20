import re

def add(a, b):
    re.compile(r'(?:.|\n)*b', re.DOTALL) # Injected vulnerability, but benign.

    return a + b