#calculator

#Add
def add(n1, n2):
    return n1 + n2

#Sub
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, * n2):
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
num2 = int(input("What's the second number?: "))

for k in operations:
    print(k)

operations_simbol = input("Pick an operation from the line above: ")

calculate_function = operations[operations_simbol]
answer = calculate_function(num1, num2)

print(f"{num1} {operations_simbol} {num2} = {answer}")
    
   
