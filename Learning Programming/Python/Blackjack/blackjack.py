import random

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    chosenCard = random.choice(cards)
    return chosenCard

def calculate_score(card_list):
    listTotal = sum(card_list)
    if listTotal == 21 and len(card_list) == 2:
        return 0

    if listTotal > 21 and 11 in card_list:
        acePosition = card_list.index(11)
        card_list[acePosition] = 1
    
    return sum(card_list)

def compare(player_score, computer_score):
    if player_score == computer_score:
        print("You tied.")
    elif player_score == 0:
        print("Blackjack, you win.")
    elif computer_score == 0:
        print("Opponent blackjack, you loose.")
    elif player_score > 21:
        print("You went over, you loose.")
    elif computer_score > 21: 
        print("Opponent went over, you win.")
    elif computer_score < player_score:
        print("You win.")
    else:
        print("You loose.")
    
def blackjack():
    player_cards = []
    computer_cards = []
    playerScore = 0
    computerScore = 0
    game_on = True

    for i in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_on:
        playerScore = calculate_score(player_cards)
        computerScore = calculate_score(computer_cards)
        print(f"Your cards are {player_cards}, current score: {playerScore}")
        print(f"Computer's first card: {computer_cards[0]}")
        if playerScore == 0 or computerScore == 0 or playerScore > 21:
            game_on = False
        else:
            if input("Do you want another card? y or n: ") == "y":
                player_cards.append(deal_card())
            else:
                game_on = False
    
    while computerScore != 0 and sum(computer_cards) < 17:
        computer_cards.append(deal_card())

    print(f"Your cards are {player_cards}, current score: {playerScore}")
    print(f"Computer's final hand: {computer_cards}, computer score: {computerScore}")
    compare(playerScore, computerScore)
    onceMore = input("Do you want to play another round? y or n ")
    if onceMore == "y":
        blackjack()
    


def main():
    blackjack()

if __name__ == "__main__":
  main()

