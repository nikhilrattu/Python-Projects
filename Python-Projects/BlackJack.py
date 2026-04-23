import random

logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def calculate_score(cards):
    """ take a list of cards and return the score 
    calculated from the cards"""
    # if 11 in cards and 10 in cards and len(cards)==2:
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)



def deal_cards():
    """ returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def compare(u_score,c_score):
    if u_score==c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack"
    elif u_score==0:
        return "Win with a Blackjack"
    elif u_score>21:
        return "You went over. You lose"
    elif c_score>21:
        return "Opponent went over. You win"
    elif u_score > c_score:
        return "you win"
        
def play_game():
    print(logo)
    user_card=[]
    comp_card=[]
    end_game=False
    for _ in range(2):
        user_card.append(deal_cards())
        comp_card.append(deal_cards())

    while not end_game:
        user_score=calculate_score(user_card)
        comp_score=calculate_score(comp_card)    
        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer's first card: {comp_card[0]}")
        if user_score==0 or comp_score==0 or user_score>21:
            end_game=True
        else: 
            extra_card=input("Type 'y'  to get another card, type 'n' " \
            "to pass: ")
            if extra_card=="y":
                user_card.append(deal_cards())
            else: 
                end_game=True

    while comp_score!=0 and comp_score<17:
        comp_card.append(deal_cards())
        comp_score=calculate_score(comp_card)
    print(f"Your final hand: {user_card}, final score: {user_score}")
    print(f"Comp's final hand: {comp_card}, final score: {comp_score}")

    print(compare(user_score,comp_score))



while input("Do you wanna play a game of blackjack? Type 'y' or 'n': ") =="y":
    print("\n" * 20)
    
    play_game()