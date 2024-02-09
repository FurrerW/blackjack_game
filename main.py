import random

def create_deck():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = [(value, suit) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    value = 0
    for card in hand:
        if card[0] in ["J", "Q", "K"]:
            value += 10
        elif card[0] == "A":
            value += 11
        else:
            value += int(card[0])
    return value

def play_again():
    play_again = input("Would you like to play again? Y/N: ").upper()
    if play_again == "Y":
        play_blackjack()
    if play_again == "N":
        print("Thanks for playing!")

def play_blackjack():
    deck = create_deck()
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    while True:
        print(f"Your hand has a value of: {calculate_hand_value(player_hand)}")
        print(f"The Dealer's hand has a value of {calculate_hand_value(dealer_hand)}")
        if calculate_hand_value(player_hand) > 21:
            print("Player busts! Dealer wins.")
            play_again()
            break
        action = input("Do you want to hit? Y/N: ").upper()
        if action == 'Y':
            player_hand.append(deal_card(deck))
        elif action == 'N':
            break

    if calculate_hand_value(player_hand) <= 21:
        while calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))
        print(f"The Dealer's hand has a value of {calculate_hand_value(dealer_hand)}")
        if calculate_hand_value(dealer_hand) > 21 or calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
            print("Player wins!")
            play_again()
        elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
            print("Dealer wins!")
            play_again()
        else:
            print("It's a tie!")
            play_again()

if __name__ == "__main__":
    play_blackjack()