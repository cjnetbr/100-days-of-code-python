from art import logo
import random
import os

def deal_card():
    ''' a deal_card() function that uses the List below to *return* a random card.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    '''
    1 - takes a List of cards as input and returns the score.
    2 - check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead 
    of the actual score. 0 will represent a blackjack in our game.
    3 - calculate_score() check for an 11 (ace). If the score is already over 21, remove 
    the 11 and replace it with a 1. 
    '''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)            

def compare(user_score, computer_score):
    if user_score == computer_score:
        return f"Draw!"
    elif computer_score == 0:
        return f"Loses, oppoent has Blackjack"
    elif user_score == 0:
        return f"Wins with a Blackjack"
    elif user_score > 21:
        return f"You went over> You lose"
    elif computer_score > 21:
        return f"Opponent went over. You win!!"
    elif user_score > computer_score:
        return f"You win!!"
    else:
        return f"You lose!!"

def play_game():
    '''Distribua 2 cartas ao usuário e ao computador'''
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    print(logo)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"You card is {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and  computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(f"Your final hand: {user_cards}, final score : {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score : {computer_score}")   
    print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == "y":
    os.system('cls' if os.name == 'nt' else 'clear')
    play_game()