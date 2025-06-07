# patterns.py

def lower_triangle(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        line = "* " * i
        result.append(line.rstrip())
    return result

def upper_triangle(n: int) -> list[str]:
    result = []
    for i in range(n):
        line = "  " * i + "* " * (n - i)
        result.append(line.rstrip())
    return result

def pyramid(n: int) -> list[str]:
    result = []
    for i in range(n):
        space = " " * (n - i - 1)
        stars = "* " * (i + 1)
        line = space + stars
        result.append(line.rstrip())
    return result

