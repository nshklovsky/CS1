import random
import sys

while True:
    
    game_type = str.lower(input("Play rock paper scissors! Would you like to play singleplayer or twoplayer?"))
    if game_type == "singleplayer":

       
        user_score = 0
        computer_score = 0
        
        while True:

            if user_score == 5:
                print("You won the game! Thanks for playing")
                break
            elif computer_score == 5:
                 print("The computer won the game! Better luck next time")
            else:
        
                user_action = str.lower(input("Enter a choice (rock, paper, scissors): "))
                possible_actions = ["rock", "paper", "scissors"]
                computer_action = random.choice(possible_actions)
                print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

                if user_action == computer_action:
                    print(f"Both players selected {user_action}. It's a tie!")
                elif user_action == "rock":
                    if computer_action == "scissors":
                        print("Rock smashes scissors! You win!")
                        user_score+=1
                    else:
                        print("Paper covers rock! You lose.")
                        computer_score+=1
                elif user_action == "paper":
                    if computer_action == "rock":
                        print("Paper covers rock! You win!")
                        user_score+=1
                    else:
                        print("Scissors cuts paper! You lose.")
                        computer_score+=1
                elif user_action == "scissors":
                    if computer_action == "paper":
                        print("Scissors cuts paper! You win!")
                        user_score+=1
                    else:
                        print("Rock smashes scissors! You lose.")
                        computer_score+=1

                else:
                    print("Invalid answer.")

                print(f"user score: {user_score} - computer score: {computer_score}")

                play_again = input("Play again? (y/n): ")
                if play_again.lower() == "y":

                    
                     break

                 elif play_again.lower() == "n":
                      print("Thanks for playing")
                      sys.exit()
        

                 else:
                     print("Invalid answer.")
                     break
                  
                   
                    

    elif game_type == "twoplayer":

        user1_score = 0
        user2_score = 0
        while True:

            if user1_score == 5:
                print("User 1 wins! Thanks for playing")
                break
            elif user2_score == 5:
                print("User 2 wins! Thanks for playing")
            else:
        
                user1_action = str.lower(input("User 1,enter a choice (rock, paper, scissors): "))
                possible_actions = ["rock", "paper", "scissors"]
                for i in range(100):
                    print("\n")
                user2_action = input("User 2,enter a choice (rock, paper, scissors): ")
                print(f"\nUser 1 chose {user1_action}, User 2 chose {user2_action}.\n")

                if user1_action == user2_action:
                    print(f"Both players selected {user1_action}. It's a tie!")
                elif user1_action == "rock":
                    if user2_action == "scissors":
                        print("Rock smashes scissors! You win!")
                        user1_score+=1
                    else:
                        print("Paper covers rock! You lose.")
                        user2_score+=1
                elif user1_action == "paper":
                    if user2_action == "rock":
                        print("Paper covers rock! You win!")
                        user1_score+=1
                    else:
                        print("Scissors cuts paper! You lose.")
                        user2_score+=1
                elif user1_action == "scissors":
                    if user2_action == "paper":
                        print("Scissors cuts paper! You win!")
                        user1_score+=1
                    else:
                        print("Rock smashes scissors! You lose.")
                        user2_score+=1
                else:
                    print("Inavlid answer.")

                print(f"User 1 score: {user1_score} - User 2 score: {user2_score}")

                play_again = input("Play again? (y/n): ")
                if play_again.lower() == "y":

                    
                    break

                elif play_again.lower() == "n":
                      print("Thanks for playing")
                      sys.exit()
        

                else:
                    print("Invalid answer.")
                    break
                  

    else:
        print("Invalid Answer")
        
        

    

    

