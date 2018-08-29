from os import system, name
from random import randint
from getpass import getpass

def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def evalProb(list):
    sums = [0]
    for i in range(0, len(list)):
        sums.append(sums[i] + list[i])
    rand = randint(0, sums[-1] - 1)
    print(sums)
    print(rand)
    for i in range(1, len(list)):
        if rand >= sums[i-1] and rand < sums[i]:
            return i
    return len(list)

def readWeights():
    weights = open("nim_weights.txt", 'r')
    vetW = []
    for i in range(0, 21):
        aux = []
        for j in range(0, 3):
            aux.append(int(weights.readline()))
        vetW.append(aux)
    weights.close()
    return vetW

def writeWeights(vetW):
    weights = open("nim_weights.txt", 'w')
    for i in range(0, 21):
        for j in range(0, 3):
            weights.write(str(vetW[i][j])+'\n')
    weights.close()

def giveReward(vetW, vetMoves, reward):
    for i in range(0, 21):
        if vetMoves[i] != 0 and vetW[i][vetMoves[i] - 1] + reward >= 1:
            vetW[i][vetMoves[i] - 1] += reward


def menuStart():
    clearScreen()
    menu = open("nim_menu.txt", 'r')
    for line in menu:
        print(line[:-1])
    menu.close()
    getpass("")

def menuWhoStarts():
    inp = 0
    invalid = False
    while inp != 1 and inp != 2:
        clearScreen()
        print("Who do you want to start the game:")
        print()
        print("1 - You")
        print("2 - NIM-ML")
        print()
        if invalid:
            print("Invalid input")
        else:
            print()
        inp = input("Type your answer: ")
        try:
            inp = int(inp)
            if inp != 1 and inp != 2:
                invalid = True
        except ValueError:
            inp = 0
            invalid = True
    return inp

def menuGame(nPieces, took):
    inp = 0
    invalid = False
    while inp < 1 or inp > 3 :
        clearScreen()
        if took != 0:
            print("NIM-ML took %d pieces" % took)
        inp = 1
        if nPieces > 0:
            print("There are %d pieces left\n" % nPieces)
            str = ""
            for i in range(0, nPieces):
                str += " |"
            print(str)
            print()
            if invalid:
                print("Invalid input")
            else:
                print()
            inp = input("How many pieces do you want to take? (1, 2 or 3)\n")
            try:
                inp = int(inp)
                if inp < 1 or inp > 3:
                    invalid = True
            except ValueError:
                inp = 0
                invalid = True
        else:
            print("There are 0 pieces left\n")
            print()
            print()
            print()
    if n - inp >= 0:
        return inp
    else:
        return n

repeat = 1
menuStart()
while repeat == 1:
    n = 21
    playerWon = False
    vetMoves = [0] * 21
    vetW = readWeights()
    start = menuWhoStarts()
    x = 0
    if start == 2:
        x = evalProb(vetW[n-1])
        vetMoves[n-1] = x
        n -= x
        playerWon = True
    while n > 0:
        inp = menuGame(n, x)
        n -= inp
        playerWon = False
        x = 0
        if n != 0:
            x = evalProb(vetW[n-1])
            vetMoves[n-1] = x
            n -= x
            playerWon = True
    menuGame(n, x)
    if playerWon:
        reward = -1
        print("You won! Congratulations!")
    else:
        reward = 1
        print("NIM-ML won!")
    giveReward(vetW, vetMoves, reward)
    getpass("Press Enter to continue...")
    writeWeights(vetW)

    repeat = 0
    invalid = False
    while repeat != 1 and repeat != 2:
        clearScreen()
        print("Would you like to restart the game?")
        print()
        print("1 - Yes")
        print("2 - No")
        print()
        if invalid:
            print("Invalid input")
        else:
            print()
        repeat = input("Type your answer: ")
        try:
            repeat = int(repeat)
            if repeat != 1 and repeat != 2:
                invalid = True
        except ValueError:
            repeat = 0
            invalid = True
clearScreen()
