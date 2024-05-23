'''
Instruções
Você vai escrever um programa que adiciona um travel_log. Você pode ver um travel_log que é uma 
lista que contém 2 dicionários. Seu trabalho é criar uma função que possa adicionar novos países 
a esta lista.

Escreva uma função que funcionará com a seguinte linha de código na linha 21 para adicionar a 
entrada do Brasil ao travel_log.

add_new_country("Brasil", 5, ["São Paulo", "Rio de Janeiro"])

NÃO modifique o travel_log diretamente. O objetivo é criar uma função que o modifique.

Exemplo de entrada

Brazil
5
["Sao Paulo", "Rio de Janeiro"]

Example Output
I've been to Brazil 5 times.
My favourite city was Sao Paulo.

Dica
- Observe a chamada de função acima para ver qual deve ser o nome da função.
- As entradas para a função são argumentos posicionais. A ordem é muito importante.
- Sinta-se à vontade para escolher seus próprios nomes de parâmetros.

'''
country = input("Add country name: \n") # Add country name
visits = int(input("Number of visits: \n")) # Number of visits
list_of_cities = eval(input("create list from formatted string: \n")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# STEP: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(country, visits, list_of_cities):
   new_country= {}
   new_country["country"] = country
   new_country["visits"] = visits
   new_country["cities"] = list_of_cities
   
   travel_log.append(new_country)
   
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
