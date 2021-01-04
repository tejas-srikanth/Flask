def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

def operation(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "Invalid operator passed"

print(operation(1, 3, 5, 7, operator="*"))