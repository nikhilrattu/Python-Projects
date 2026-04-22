

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

operations={
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": division
}
def calculate():
    cont=True

    num1 = float(input("Enter the first number: "))
    while cont:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Enter the operation: ")
        num2 = float(input("Enter the second number: "))
        answer=operations[operation_symbol](num1, num2)
        print(f"{num1} + {num2} = {answer}")

        choice=input("Do you want to calculate another number"
                     " with keeping the result as first "
                     "number? type (y/n): ")
        if choice == "y":
            num1=answer
        else:
            cont=False
            print("\n" * 100)
            calculate()

calculate()