import random

def play_game():
    options =  {"rock": "rock", "paper": "paper", "scissors": "scissors"}
    score = {"wins": 0, "losses": 0, "draws": 0}

    print("GARENA PRODUCTIONS")
    print("***************-:Rules:-****************")
    print(" - ROCK beats SCISSORS ")
    print(" - PAPER beats ROCK")
    print(" - SCISSORS beats PAPER")
    print("Enter 'rock', 'paper,' or 'scossors' to play.")
    print("Enter 'b', for back game.")
    print()


    while (True):
        user_choice = input("Enter your choice : ").lower()
        
        if user_choice == 'b':
            print("Game ended...")
            total_games = score ["wins"] + score["losses"] + score["draws"]
            win_rate = (score["wins"] / total_games * 100) if total_games > 0 else 0
            print(f"Yours Final Score - wins : {score['wins']}, Losses : {score['losses']}, Draws : {score['draws']}")
            print(f"Win rate : {win_rate:.2f}%")
            break
        
        elif user_choice not in options:
            print("Invalid choice, pls try again.")
            continue
        
        player = options[user_choice]
        opponent = random.choice(["rock", "paper", "scissors"])
        print(f"Opponent choice : {opponent}")
        
        
        if opponent == player:
           print("Game Draw")       
           score["draws"] += 1
        else:
           if (opponent == "rock" and player == "paper") or (opponent == "paper" and player == "scissors") or (opponent == "scissros" and player == "rock"):
            
                print("You win")
                score["wins"] += 1
           else:
                print("You lose")
                score["losses"] += 1
               
        total_games = score ["wins"] + score["losses"] + score["draws"]
        win_rate = (score["wins"] / total_games * 100) if total_games > 0 else 0        
        print(f"Current Score - wins : {score['wins']}, Losses : {score['losses']}, Draws : {score['draws']}")
        print(f"Win rate : {win_rate:.2f}%")
        print()
play_game()