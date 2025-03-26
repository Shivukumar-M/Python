# Rock,paper,scissor game
import random

def game():
    print("\nWelcome to Rock ,Paper ,Scissor!")

    # Loop to allow replaying the game
    while True:   
        choices=["rock","paper","scissor"]
        player_win=0
        computer_win=0
        for round_num in range(1,4): # You can play 3 round
            print(f"Round {round_num} :")
            player_choice=input("Enter your choice(Rock,Paper,scissor):").lower()
            # player_choice.lower()

            if player_choice not in choices:
                print("invalid choice Please try again")
                continue # Restart the loop for the same round
            
            computer_choice=random.choice(choices)
            print(f"Computer choice:{computer_choice}")

            if player_choice ==computer_choice:
                print("It's a Draw/Tie")
            elif (player_choice=="rock" and computer_choice=="scissor") or \
                (player_choice=="paper" and computer_choice=="rock") or \
                (player_choice=="scissor" and computer_choice=="paper"):
                print("You won this round")
                player_win +=1
            else:
                print("You lost this round")
                computer_win +=1
        
        #display the final result
        print("\nFinal Results:")
        print(f"You won: {player_win}")
        print(f"computer won:{computer_win}")

        if player_win > computer_win:
            print("🎉 Congratulations! You won the game!")
        elif player_win < computer_win:
            print("💻 Computer wins the game! Better luck next time.")
        else:
            print("🤝 It's a Tie!")
        
    # Ask the user if they want to play again
        newround = input("\nDo you want to play again?\n1) Continue\n2) Quit\nEnter your choice: ")
            
        if newround != "1":  # If input is not "1", exit the loop
            print("You have quit the game. Goodbye!")
            break        

   #THe game starts now
game()
