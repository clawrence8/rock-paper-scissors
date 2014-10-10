from random import*

def rps():
    players = input("Welcome to Rock, Paper, Scissors! Press 1 for One Player or 2 for Two Players")
    cpu = randint(0,99)
    if cpu >= 0 and cpu <33:
        cpu_choice = "rock"
    elif cpu >= 33 and cpu <66:
        cpu_choice = "paper"
    else:
        cpu_choice = "scissors"
    if players == "1": #One Player Mode
        user1 = input("Please enter your name")
        choice = input("Choose: Rock, Paper, or Scissors")
        if choice.lower() == "rock":
            if cpu_choice == "rock":
                print("CPU chose", cpu_choice)
                print("Tie!")
            elif cpu_choice == "paper":
                print("CPU chose", cpu_choice)
                print("CPU wins! Do better next time")
            else:
                print("CPU chose", cpu_choice)
                print(user1, "you won!")
        elif choice.lower() == "paper":
            if cpu_choice == "rock":
                print("CPU chose", cpu_choice)
                print(user1, "you won!")
            elif cpu_choice == "paper":
                print("CPU chose", cpu_choice)
                print("Tie!")
            else:
                print("CPU chose", cpu_choice)
                print("Sorry",user1, "the CPU won. Get Better!")
        elif choice.lower() == "scissors":
            if cpu_choice == "rock":
                print("CPU chose", cpu_choice)
                print("Sorry",user1, "the CPU won. Get Better!")
            elif cpu_choice == "paper":
                print("CPU chose", cpu_choice)
                print(user1, "you won!")
            else:
                print("CPU chose", cpu_choice)
                print("Tie!")
        else:
            print("Invalid answer. Try again with 'rock', 'paper', or 'scissors'")
            rps()
    elif players == "2": #Two Player Mode
        user1 = input("Player 1, please enter your name")
        user2 = input("Player 2, please enter your name")
        choice1 = input(user1, "choose: Rock, Paper, or Scissors")
        choice2 = input(user2, "choose: Rock, Paper, or Scissors")
        if choice2.lower() != "rock" and choice2.lower() != "paper" and choice2.lower() != "scissors":
            print("Invalid answer. Try again with 'rock', 'paper', or 'scissors'")
            rps()
        if choice1.lower() == "rock":
            if choice2 == "rock":
                print(user2, "chose", choice2)
                print("Tie!")
            elif choice2 == "paper":
                print(user2, "chose", choice2)
                print(user2, "wins!")
            else:
                print(user2, "chose", choice2)
                print(user1, "you won!")
        elif choice1.lower() == "paper":
            if choice2 == "rock":
                print(user2, "chose", choice2)
                print(user1, "you won!")
            elif choice2 == "paper":
                print(user2, "chose", choice2)
                print("Tie!")
            else:
                print(user2, "chose", choice2)
                print("Sorry",user1+",",user2,"won.")
        elif choice2 == "scissors":
            if choice2 == "rock":
                print(user2, "chose", choice2)
                print("Sorry",user1+",", user2, "won.")
            elif chocie2 == "paper":
                print(user2, "chose", choice2)
                print(user1, "you won!")
            else:
                print(user2, "chose", choice2)
                print("Tie!")
        else:
            print("Invalid answer. Try again with 'rock', 'paper', or 'scissors'")
            rps()
    else:
        print("Invalid answer. You may only have 1 or 2 players")
        rps()