cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random

def check(user_sum, dealer_sum):
    if user_sum <= 21 and dealer_sum <= 21 and user_sum > dealer_sum:
        print("You win")
    elif user_sum <= 21 and dealer_sum <= 21 and user_sum < dealer_sum:
        print("Dealer wins")
    elif user_sum <= 21 and dealer_sum <= 21 and user_sum == dealer_sum:
        print("Its a draw")
    elif user_sum > 21 and dealer_sum <= 21:
        print("Dealer wins")
    elif user_sum <= 21 and dealer_sum > 21:
        print("User wins")
    elif user_sum > 21 and dealer_sum > 21:
        dealer_sum1 = dealer_sum - 21
        user_sum1 = user_sum - 21
        if dealer_sum1 > user_sum1:
            print("You win")
        elif dealer_sum1 < user_sum1:
            print("Dealer wins")

def draw_cards1():
    decision = input("To start game type 'y' and to exit game type 'n'.")
    if decision == "n":
        print("Thank you for playing")
    while decision == 'y':
        draw_cards = {}
        draw_cards["user"] = [random.choice(cards), random.choice(cards)]
        draw_cards["handler"] = [random.choice(cards), random.choice(cards)]
        print(f"your hand is {draw_cards['user']}.")
        print(f"dealers hand is {draw_cards['handler'][0]}")
        direction = input("if you want to draw type 'd' and to hold type 'h'.")
        if direction == "d":
            draw_cards["user"].append(random.choice(cards))
            draw_cards["handler"].append(random.choice(cards))
            print(f"Your hand is {draw_cards['user']}.")
            print(f"Dealers hand is {draw_cards['handler']}")
            check(sum(draw_cards["user"]), sum(draw_cards["handler"]))
            draw_cards1()
            break
        elif direction == "h":
            print(f"Your hand is {draw_cards['user']}.")
            print(f"Dealers hand is {draw_cards['handler']}.")
            check(sum(draw_cards["user"]), sum(draw_cards["handler"]))
            draw_cards1()
            break

draw_cards1()