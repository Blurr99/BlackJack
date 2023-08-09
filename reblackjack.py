import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_card(player):
    player.append(random.choice(cards))

def go():
    go = int(input("Press 1 to play again and 0 to exit. "))
    if go == 1:
        blackjack()
    else:
        os.system('cls')
        exit()


def blackjack():
    os.system('cls')
    print(logo)
    user = []
    dealer = []

    draw_card(user)
    draw_card(user)
    draw_card(dealer)
    draw_card(dealer)

    shouldContinue = 1
    while shouldContinue:
        userscore = sum(user)
        dealerscore = sum(dealer)
        print(f"Your cards: {user}, current score: {userscore}")
        print(f"Computer's first card: {dealer[0]}")
        while userscore < 21:
            choice = input("Type 'y' to get another card or 'n' to pass: ")
            if choice == "y" or userscore<17:
                if userscore < 17 and choice == "n":
                    print("\nYour score is less than 17 so you have to pick another card!!!")
                # user.append(random.choice(cards))
                draw_card(user)
                userscore = sum(user)
                if userscore<21:
                    print(f"\nYour cards: {user}, current score: {userscore}")
                    print(f"Computer's first card: {dealer[0]}")
            elif choice == "n":
                print(f"\nYour cards: {user}, current score: {userscore}")
                dealerscore = sum(dealer)
                # print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
                break
        if userscore>21:
            print(f"\nYour cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Lose!!!")
            go()
            
        if userscore == 21:
            print(f"\nYour cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Win!!!")
            go()
        while dealerscore<17:
            # dealer.append(random.choice(cards))
            draw_card(dealer)
            dealerscore = sum(dealer)
        print(f"Dealer's cards: {dealer} with score: {dealerscore}")
        if dealerscore > 21:
            print(f"Your cards: {user}, current score: {userscore}")
            # print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Win!!!")
            go()
        elif userscore > dealerscore:
            print(f"\nYour cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Win!!!")
            go()
        elif dealerscore > userscore:
            # print(f"Your cards: {user}, current score: {userscore}")
            # print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Lose!!!")
            go()
        else:
            # print(f"Your cards: {user}, current score: {userscore}")
            # print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("DRAW")
            go()

blackjack()