############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Press 'y' if you wanna play and 'n' if you don't wanna: ")

def clear(): 
      # for windows 
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

def deal_card():
    card = random.choice(cards)
    return card


def calculate_score(player):
        score = sum(player)
        if score == 21 and len(player) == 2:
            score = 0

        if score > 21 and 11 in player:
            player.remove(11)
            player.append(1)
            score = sum(player)
        
        return score


def compare(user_score, dealer_score):
    if user_score > 21 and dealer_score > 21:
        print ("Y'all both lose")
    elif user_score > 21:
        print ("Player goes bust ! Dealer wins")
    elif dealer_score > 21:
        print ("Dealer goes bust ! Player wins")
    elif user_score > dealer_score and user_score <= 21:
        print ("Player Wins")
    elif dealer_score > user_score and dealer_score <= 21:
        print ("Dealer Wins")
    elif user_score == dealer_score:
        print ("Draw game !")


def play_blackjack():
    print (art.logo)
    user_cards = []
    dealer_cards = []

    for n in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
   

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    if user_score == 0:
        print ("You win, Blackjack !")
    if dealer_score == 0:
        print ("You lose, dealer Blackjack")

    keep_drawing = True

    print (f"Your current hand is {user_score} consisting {user_cards}")
    print (f"Dealer first card is {user_cards[0]}")

    while user_score < 21 and keep_drawing == True:
        draw_card = input("Type 'draw' to draw a card or anything else to pass: ")
        if draw_card == 'draw':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print (f"Your current hand is {user_score} consisting {user_cards}")
        else: 
            keep_drawing = False

    if user_score > 21:
        print ("You went bust !")

    print (f"Dealer current hand is {dealer_score} consisting {dealer_cards}")    

    while dealer_score < 17 and dealer_score != 0:
        print ("Dealer draws a card")
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print (f"Dealer current hand is {dealer_score} consisting {dealer_cards}")

    compare(user_score, dealer_score)

while play == 'y':
    play_blackjack()
    play = input("Play again ? 'y', n' ?: ")
    if play == 'y':
        clear()
    else:
        play = 'n'
    

