from art import logo
import random

'''
Crie uma função deal_card() que use a lista abaixo para *retornar* um cartão aleatório.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

'''
def deal_card():
    ''' a deal_card() function that uses the List below to *return* a random card.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list):
    '''
    1 - takes a List of cards as input and returns the score.
    2 - check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead 
    of the actual score. 0 will represent a blackjack in our game.
    3 - calculate_score() check for an 11 (ace). If the score is already over 21, remove 
    the 11 and replace it with a 1. 
    '''
    score = sum(list)
    if 11 in list:
        if score > 21:
            list.remove(11)
            list.append(1)
            score = sum(list)
    
    blackjack = 21
    if score == blackjack:
        score = 0
        return score
    else:
        return score            

    
'''Distribua 2 cartas ao usuário e ao computador'''
user_card = []
computer_card = []
u_final_hand = []
c_final_hand = []

for c in range(2):
    uc = deal_card()
    user_card.append(uc)
    cc = deal_card()
    computer_card.append(cc)

print(logo)
user_score = calculate_score(user_card)
computer_score = calculate_score(computer_card)

print(f"You card is {user_card}, current score: {user_score}")
print(f"Computer's first card: {computer_card[0]}")

if user_score == 0:
    u_final_hand = user_card
    print(f"Your final hand: {u_final_hand}, final score : {user_score}")
    print(f"Computer's final hand: {c_final_hand}, final score : {computer_score}")
    print("Win with a Blackjack")
elif computer_score == 0:
    c_final_hand = computer_card
    print(f"Computer's final hand: {c_final_hand}, final score : {computer_score}")
    print(f"Your final hand: {u_final_hand}, final score : {user_score}")
    print("Computer's win with a Blackjack")
    

end_game = False

while not end_game:
    n_card = input(f"Type 'y' to get another card, type 'n' to pass: ")
    if n_card == "y":
        nc = deal_card()
        user_card.append(nc)
        new_score = calculate_score(user_card)
        if new_score > 21:
            print(f"You card is {user_card}, current score: {calculate_score(user_card)}")
            print(f"Computer's first card: {computer_card[0]}")
            u_final_hand = user_card
            c_final_hand = computer_card
            print(f"Your final hand: {u_final_hand}, final score : {new_score}")
            print(f"Computer's final hand: {c_final_hand}, final score : {computer_score}")
            end_game = True
    elif n_card == "n":
        while computer_score <= 17:
            nc = deal_card()
            computer_card.append(nc)
            new_score = calculate_score(computer_card)
        end_game = True

            
print(user_card, computer_card)
