import art

## Calculator Functions
def calculate(operation, n1,n2):
    if operation == "+":
        return n1 + n2
    if operation == "-":
        return n1 - n2
    if operation == "*":
        return n1 * n2
    if operation == "/":
        return n1 / n2

operations = ["+","-","*","/"]

def calculator():
    print (art.logo)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print (symbol)

    should_continue = True
    
    while should_continue:
        operation_symbol = input("Pick and operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        answer = calculate(operation_symbol, num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        ending = input(f"Type 'y' to continue, 'n' to reset calculator, 'exit' to exit the calculator: ")

        if ending == "y":
            num1 = answer
        elif ending == "n":
            should_continue = False
            calculator()
        elif ending == 'exit':
            should_continue = False

calculator()