''' 
Instruções
Converta a função is_leap()

No código inicial, você encontrará a solução do desafio do ano bissexto. Primeiro, converta esta função 
is_leap() para que em vez de imprimir "Ano bissexto." ou "Não é ano bissexto". deve retornar True se for 
um ano bissexto e retornar False se não for um ano bissexto.

Crie uma nova função chamada days_in_month()

Em seguida, você modificará uma função chamada days_in_month() que levará um ano e um mês como entradas, 
por exemplo.

dias_no_mês(ano=2022, mês=2)
E usará essas informações para descobrir se o ano é bissexto e decidir o número de dias do mês, depois 
retornará isso como resultado, por exemplo:

28

A lista mês_dias contém o número de dias em um mês de janeiro a dezembro para um ano não bissexto. 
Um ano bissexto tem 29 dias em fevereiro.

Dica
Observe a chamada de função na parte inferior do código para ver os argumentos posicionais. A ordem é 
muito importante.

Sinta-se à vontade para escolher seus próprios nomes de parâmetros.

Lembre-se de que mês_dias é uma lista e as listas em Python começam na posição 0. Portanto, o número de 
dias em janeiro é mês_dias[0]

Tenha cuidado com o recuo.

'''

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        #print("Leap year")
        return True
      else:
        #print("Not leap year")
        return False
    else:
      #print("Leap year")
      return True
  else:
    #print("Not leap year")
    return False
  
# STEP: Add more code here 👇
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year):
      month_days[1] = 29
      return month_days[month - 1]
  else:
      return month_days[month - 1]
   

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year")) # Enter a year
month = int(input("Enter a month")) # Enter a month
days = days_in_month(year, month)
print(days)
#leap_year = is_leap(year)
#print(leap_year)

