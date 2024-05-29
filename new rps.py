import random
import sys

rps_list = ["rock","paper","scissors"]

while True:
    user_play = str.lower(input("Would you like to play rps? "))

    if user_play == "yes":
        user_score = 0
        bot_score = 0
        score_limit = 5

        while user_score < score_limit and bot_score < score_limit:
            user_action = str.lower(input("\nchoose an option, rock, paper, or scissors "))
            bot_action = random.choice(rps_list)

            if user_action == "end":
                print("thanks for playing!")
                sys.exit()
            elif user_action not in rps_list:
                print("Invalid Answer")
            else:
                print(f"You chose {user_action} while the bot chose {bot_action}")

                if user_action == bot_action:
                    print("Both chose the same option, tie!")
                elif user_action == "rock":
                    if bot_action == "paper":
                        print("You lose")
                        bot_score += 1
                    elif bot_action == "scissors":
                        print("You win")
                        user_score += 1
                elif user_action == "paper":
                    if bot_action == "scissors":
                        print("You lose")
                        bot_score += 1
                    elif bot_action == "rock":
                        print("You win")
                        user_score += 1
                elif user_action == "scissors":
                    if bot_action == "rock":
                        print("You lose")
                        bot_score += 1
                    elif bot_action == "paper":
                        print("You win")
                        user_score += 1
                print(f"The current score is: You - {user_score} | bot - {bot_score}")

        if user_score > bot_score:
            print("You won this game!")
        elif user_score < bot_score:
            print("Sorry, the bot won this game!")
        else:
            print("It was a tie")
    elif user_play == "no":
        print("bye")
        break
    else:
        print("Invalid Answer")




        

    


