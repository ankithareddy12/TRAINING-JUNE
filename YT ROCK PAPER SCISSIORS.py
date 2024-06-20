import random
def get_game():
    player_choice=input()
    options=['rock','paper','scissors']
    computer_choice=random.choice(options)
    choices={"player":player_choice ,"computer":computer_choice}
    return choices
def check_win(player,computer):
    print(f"you chose {player},computer chose {computer}")
    if player==computer:
        return 'its a tie'
    elif player=="rock":
        if computer == "scissors":
            return 'players wins'
        else:
            return 'player lose'
    elif player=="paper":
        if computer == "rock":
            return 'players wins'
        else:
            return 'player lose'
    elif player=="scissors":
        if computer == "paper":
            return 'players wins'
        else:
            return 'player lose'
choices=get_game()
result=check_win(choices["player"],choices["computer"])
print(result)

