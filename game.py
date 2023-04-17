import random

print("Welcome to RPS Game")

Options = ("rock", "paper", "scissors")
playing = True

while playing:

 player = None
 computer = random.choice(Options)

 while player not in Options:
  player = input("Enter your Choice (rock, paper, scissors): ")


 print(f"Player: {player}")
 print(f"computer: {computer}")


 if player == computer:
     print("It's a tie!")
    
 elif player == "rock" and computer == "scissors":
     print("You win!")
    
 elif player == "paper" and computer == "rock":
     print("You win!")
    
 elif player == "scissors" and computer == "paper":
     print("You win!")
    
 else:
     print("You lose!")
    
    
 play_again = input("Play again? (y/n):").lower()
 if not play_again == "y":
     playing = False
        
print("Thanks For Playing")
    


   
        
        


    
    
    