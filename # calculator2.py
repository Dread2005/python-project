# calculator
from calculatorart import logo

def add(n1,n2):
    """adds two numbers together"""
    return n1 + n2

def subtract(n1,n2):
    """subtracts two numbers"""
    return n1 - n2

def multiply(n1,n2):
    """multiplys two numbers"""
    return n1 * n2

def devision(n1,n2):
    """devides two numbers"""
    return n1 / n2

operations = {
              "/" : devision,
              "*" : multiply,
              "-" : subtract,
              "+" : add,
              }
def calculator():
    print(logo)
    num1 = float(input("First number: "))

    for op in operations:
        print(op)
    y = True
    while y:
        operation_choice = input("Enter operation: ")

        num2 = float(input("Second number: "))

        calc_function = operations[operation_choice]
        answer = calc_function(num1,num2)
        print(f"{num1}{operation_choice}{num2} = {answer}")

        if input(f"Would you like to continue with {answer} type y or if not type n:" ) == "y":
            num1 = answer
        else:
            y = False
            calculator()
calculator()

    
    
    














