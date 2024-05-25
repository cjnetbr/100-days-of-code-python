#calculator

#Add
def add(n1, n2):
    return n1 + n2

#Sub
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Create a dictionary named operations
operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide 
}

num1 = int(input("What's the first number?: "))

for k in operations:
    print(k)
operations_simbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))
calculate_function = operations[operations_simbol]
#answer = calculate_function(num1, num2)
first_answer = calculate_function(num1, num2)

print(f"{num1} {operations_simbol} {num2} = {first_answer}")

operations_simbol = input("Pick another operation: ")
num3 = int(input("What's the second number?: "))
calculate_function = operations[operations_simbol] 
second_answer = calculate_function(calculate_function(num1, num2), num3)

print(f"{first_answer} {operations_simbol} {num3} = {second_answer}")

   
