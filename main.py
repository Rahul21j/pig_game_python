import random

globalScore = ["0", "0"]
currentScore = ["0", "0"]

currentPlayer = 1

cs = int(currentScore[currentPlayer - 1])
gs = int(globalScore[currentPlayer - 1])
winningScore = int(input("Enter the WINNING SCORE: "))


def next_player():
    global globalScore, winningScore, currentPlayer, gs
    if int(globalScore[currentPlayer - 1]) >= winningScore:
        print(f"Player {currentPlayer}: Won!!!")
    else:
        if currentPlayer == 1:
            currentPlayer = 2
        else:
            currentPlayer = 1
        gs = int(globalScore[currentPlayer - 1])
        logic()


def logic():
    while True:
        global globalScore, currentScore, currentPlayer, gs, cs, winningScore
        print(f"\nPlayer: {currentPlayer}")
        user = int(input("1) Roll\n2) Hold\n3) Exit\n"))
        print(f"Your choice: {user}")
        if user == 1:

            number = random.randint(1, 6)
            if number != 2:
                cs += number
                print(f"Dice: {number}")
                print(f"Current Score: {cs}")
            else:
                cs = 0
                print(f"Dice: {number}")
                print(f"Current Score: {cs}")
                break
        elif user == 2:
            gs += cs
            cs = 0
            globalScore[currentPlayer - 1] = str(gs)
            print(f'\nPlayer 1: {globalScore[0]}        Player 2: {globalScore[1]}')
            break

        elif user == 3:
            break
        else:
            print("Invalid choice\n")
    if user == 3:
        print("You exited the game.")
        return 0
    next_player()


logic()
