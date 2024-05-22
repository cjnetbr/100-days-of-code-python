'''
Instructions
Você está pintando uma parede. As instruções sobre a tinta pode dizer que 1 lata de tinta pode cobrir 5 metros quadrados de parede. Dada uma altura e largura aleatórias da parede, calcule quantas latas de tinta você precisará comprar.

número de latas = (altura da parede x largura da parede) ÷ cobertura por lata.

por exemplo, altura = 2, largura = 4, cobertura = 5

number of cans = (2 * 4) / 5
               = 1.6
Mas como você não pode comprar 0,6 de uma lata de tinta, o resultado deve ser arredondado para 2 latas.

IMPORTANTE: Observe que o nome da função e os parâmetros devem corresponder aos da linha 13 para que o código funcione.

Example Input
3
9
Example Output
You'll need 6 cans of paint.
Hint
Stackoveflow link on how to round up a number: https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python


'''
# Write your code below this line 👇
import math
def paint_calc(height, width, cover ):
    number_cans = ( height * width) / cover
    return print(f"You'll need {math.ceil(number_cans)} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall (m)")) # Height of wall (m)
test_w = int(input("Width of wall (m)")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

