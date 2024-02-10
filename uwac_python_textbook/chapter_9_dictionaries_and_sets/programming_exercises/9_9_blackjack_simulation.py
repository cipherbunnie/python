# Author: Vam
# Date: 14/01/2024

'''
Previously in this chapter you saw the card_dealer. py program that
simulates cards being dealt from a deck. Enhance the program so it simulates a
simplified version of the game of Blackjack between two virtual players. The
cards have the following values:
    • Numeric cards are assigned the value they have printed on them. For
    example, the value of the 2 of spades is 2, and the value of the 5 of
    diamonds is 5.
    • Jacks, queens, and kings are valued at 10.
    • Aces are valued at 1 or 11, depending on the player's choice.
    
The program should deal cards to each player until one player's hand is worth
more than 21 points. When that happens, the other player is the winner. (It is
possible that both players' hands will simultaneously exceed 21 points, in
which case neither player wins.) The program should repeat until all the cards
have been dealt from the deck.

If a player is dealt an ace, the program should decide the value of the card
according to the following rule: The ace will be worth 11 points, unless that
makes the player's hand exceed 21 points. In that case, the ace will be worth 1
point.
'''

import random

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        rank = card['rank']
        if rank.isdigit():
            value += int(rank)
        elif rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            num_aces += 1
            value += 11

    # Adjust the value for aces
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

def display_hand(player, hand):
    print(f"{player}'s hand:")
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")
    print(f"Total value: {calculate_hand_value(hand)}\n")

def blackjack():
    deck = create_deck()
    player1_hand = []
    player2_hand = []

    while deck:
        deal_card(deck, player1_hand)
        deal_card(deck, player2_hand)

        display_hand("Player 1", player1_hand)
        display_hand("Player 2", player2_hand)

        if calculate_hand_value(player1_hand) > 21 or calculate_hand_value(player2_hand) > 21:
            break

    if calculate_hand_value(player1_hand) > 21 and calculate_hand_value(player2_hand) > 21:
        print("Both players bust. It's a tie!")
    elif calculate_hand_value(player1_hand) > 21:
        print("Player 1 busts. Player 2 wins!")
    elif calculate_hand_value(player2_hand) > 21:
        print("Player 2 busts. Player 1 wins!")
    else:
        print("Both players have finished. Determining the winner...")
        if calculate_hand_value(player1_hand) > calculate_hand_value(player2_hand):
            print("Player 1 wins!")
        elif calculate_hand_value(player2_hand) > calculate_hand_value(player1_hand):
            print("Player 2 wins!")
        else:
            print("It's a tie!")

if __name__ == "__main__":
    blackjack()
