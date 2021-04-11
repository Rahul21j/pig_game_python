import random

globalScore = ["0", "0"]
currentScore = ["0", "0"]

currentPlayer = 1

temp_curr_score = 0
temp_glob_score = 0
winningScore = int(input("Enter the WINNING SCORE: "))


def next_player():
    global globalScore, winningScore, currentPlayer, temp_glob_score
    if int(globalScore[currentPlayer - 1]) >= winningScore:
        print(f"Player {currentPlayer}: Won!!!")
    else:
        if currentPlayer == 1:
            currentPlayer = 2
        else:
            currentPlayer = 1
        temp_glob_score = int(globalScore[currentPlayer - 1])
        logic()


def logic():
    while True:
        global globalScore, currentScore, currentPlayer, temp_glob_score, temp_curr_score, winningScore
        print(f"\nPlayer: {currentPlayer}")
        user = int(input("1) Roll\n2) Hold\n3) Exit\n"))
        print(f"Your choice: {user}")
        if user == 1:
            number = random.randint(1, 6)
            if number != 2:
                temp_curr_score += number
                print(f"Dice: {number}")
                print(f"Current Score: {temp_curr_score}")
            else:
                temp_curr_score = 0
                print(f"Dice: {number}")
                print(f"Current Score: {temp_curr_score}")
                break
        elif user == 2:
            temp_glob_score += temp_curr_score
            temp_curr_score = 0
            globalScore[currentPlayer - 1] = str(temp_glob_score)
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
