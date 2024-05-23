'''
Pergunta 1:
Which line of code will change the to the ?starting_dictionaryfinal_dictionary

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

'''

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary 

print(starting_dictionary)
print(final_dictionary)

''' 
Pergunta 2:
Which line of code will produce an error?

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
'''

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

#print(dict[1])

''' 
Pergunta 3:
Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

'''

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])