
import random

moves = ["rock", "paper", "scissors"]

def play():
    play_options = ["rock", "paper", "scissors"]
    play = True

    win = 0
    lose = 0
    tie = 0

    while play:
        if lose >= 5:
            dyn = input("Do you want to use dynamite?") 

            if dyn == "yes":
                    print("KABOOM!")
                    print(f"Game Results: \n win: {win} \n lose: {lose} \n tie {tie}")
                    play = False

        user_input = input("Enter (rock, paper, scissors, quit): ")
        computer_input =  (random.choice(play_options))
        print(computer_input)
                
        if user_input == "rock":
            if computer_input == "scissors":
                win += 1
                print("Rock destroyed scissors! You win!")
            elif computer_input == user_input:
                tie += 1
                print("tie")
            else:
                lose += 1
                print("Paper smothered rock to death! You lose.")

        elif user_input == "paper":
            if computer_input == "rock":
                win += 1
                print("Paper smothered rock to death! You win!")
            elif computer_input == user_input:
                tie += 1
                print("You tied!")
            else:
                lose += 1
                print("Scissors chopped paper to pieces! You lose."  )

        elif user_input == "scissors":
            if computer_input == "paper":
                win += 1
                print("Scissors chopped paper to pieces! You win!")
            elif computer_input == user_input:
                tie += 1
                print("You tied!")
            else:
                lose += 1
                print("Rock destroyed scissors! You lose.")

        elif user_input == "quit":
            print(f"Game Results: \n win: {win} \n lose: {lose} \n tie {tie}")
            play = False

print(play())
