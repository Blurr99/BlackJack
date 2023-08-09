import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():
    print(logo)
    user = []
    dealer = []
    user.append(random.choice(cards))
    user.append(random.choice(cards))
    dealer.append(random.choice(cards))
    dealer.append(random.choice(cards))


    shouldContinue = 1
    while shouldContinue:
        userscore = sum(user)
        dealerscore = sum(dealer)
        print(f"Your cards: {user}, current score: {userscore}")
        print(f"Computer's first card: {dealer[0]}")
        if userscore < 21:
            choice = input("Type 'y' to get another card or 'n' to pass: ")
            if choice == "y" or userscore<17:
                if userscore < 17:
                    print("Your score is less than 17 so you have to pick another card!!")
                user.append(random.choice(cards))
                userscore = sum(user)
            if (choice == "n" and userscore > 17) or userscore > 21:
                userscore = sum(user)
                dealerscore = sum(dealer)
                print(f"Your cards: {user}, current score: {userscore}")
                print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
                print("You Lose!!")
                shouldContinue = 0
            if dealerscore < 17:
                dealer.append(random.choice(cards))
        elif userscore == 21:
            userscore = sum(user)
            dealerscore = sum(dealer)
            print(f"Your cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Win!!")
            shouldContinue = 0
            y = int(input("Press 1 to play again. "))
            if y==1:
                os.system('cls')
                blackjack()
        elif userscore == dealerscore:
            userscore = sum(user)
            dealerscore = sum(dealer)
            print(f"Your cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("DRAW")
            shouldContinue = 0
            y = int(input("Press 1 to play again. "))
            if y==1:
                os.system('cls')
                blackjack()
        else:
            userscore = sum(user)
            dealerscore = sum(dealer)
            print(f"Your cards: {user}, current score: {userscore}")
            print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
            print("You Lose ")
            shouldContinue = 0
            y = int(input("Press 1 to play again. "))
            if y==1:
                os.system('cls')
                blackjack()


    if (userscore > dealerscore) and (userscore <= 21):
        userscore = sum(user)
        dealerscore = sum(dealer)
        print(f"Your cards: {user}, current score: {userscore}")
        print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
        print("You Win")
        y = int(input("Press 1 to play again. "))
        if y==1:
            os.system('cls')
            blackjack()
    else:
        userscore = sum(user)
        dealerscore = sum(dealer)
        print(f"Your cards: {user}, current score: {userscore}")
        print(f"Dealer's cards: {dealer}, current score: {dealerscore}")
        print("You lose")
        y = int(input("Press 1 to play again. "))
        if y==1:
            os.system('cls')
            blackjack()

    
blackjack()


