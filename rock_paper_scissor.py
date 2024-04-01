import random

while True:
    start_game = int(input("PRESS [1] TO PLAY AND [0] TO EXIT: "))
    
    if start_game == 1:
        comp_choices = ["rock","paper","scissors"]
        print("ENTER YOUR CHOICE:\n\n   1) ROCK\n   2) PAPER\n   3) SCISSORS\n")
        human_ans = input(" WRITE YOUR CHOICE: ").lower()
        print()
        comp_ans = random.choice(comp_choices)

        if human_ans not in comp_choices:
            print("INVALID INPUT\n")
            
        if comp_ans == human_ans:
            print("COMPUTER CHOICE WAS:",comp_ans)
            print()
            print("--------TIE----------\n")

        elif comp_ans == "rock" and human_ans == "scissors" or comp_ans == "scissors" and human_ans == "paper" or comp_ans == "paper" and human_ans == "rock":
            print("COMPUTER CHOICE WAS:",comp_ans)
            print()
            print("--------COMPUTER WON-------\n")

        else:
            print("COMPUTER CHOICE WAS:",comp_ans)
            print()
            print("-------YOU WON---------\n")

    elif start_game == 0:
        break 

    else:
        print("INVALID KEY ENTERED")