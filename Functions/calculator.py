def calculate(operator, a, b):
    result = None
    if operator == "multiply":
        result = a * b
    elif operator == "divide":
        result = a / b
    elif operator == "add":
        result = a + b
    elif operator == "subtract":
        result = a - b 
    return result            

operator = str(input())   
a = int(input())   
b = int(input())   

result = int(calculate(operator, a, b))

print(result)