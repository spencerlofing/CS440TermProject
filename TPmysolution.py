import copy
import random
state = [['R', 'B', 'R', 'B', 'R', 'B'], [], [], ['B'], [], [], []]

def printState(state):
    copystate = copy.deepcopy(state)
    for slot in copystate:
        slotlength = len(slot)
        for i in range(0, 6 - slotlength):
           slot.insert(0, 'X')

    for i in range(0, 6):
        temp = ''
        for slot in copystate:
            temp = temp + slot[i] + ' '
        print(temp)
    print()

def validMoves(state):
    listOfMoves = []
    for i in range(0, len(state)):
        if len(state[i]) < 6:
            listOfMoves.append(i)
    return listOfMoves

def makeMove(state, move, color):
    copystate = copy.deepcopy(state)
    copystate[move].insert(0, color)
    return copystate

def reachedGoalState(state):
    #Fill all slots for computation
    copystate = copy.deepcopy(state)
    for slot in copystate:
        slotlength = len(slot)
        for i in range(0, 6 - slotlength):
            slot.insert(0, 'X')

    #Vertical checks
    for slot in copystate:
        for i in range(0,3):
            if (slot[i] == slot[i+1]) & (slot[i] == slot[i+2]) & (slot[i] == slot[i+3]) & (slot[i] != 'X'):
                return 1

    #Horizontal checks
    for j in range(0,4):
        for i in range(0,len(copystate[0])):
            if (copystate[j][i] == copystate[j+1][i]) & (copystate[j][i] == copystate[j+2][i]) & \
                    (copystate[j][i] == copystate[j+3][i]) & (copystate[j][i] != 'X'):
                return 1

    #Diaganol up-right
    for i in range(0,4): #row
        for j in range(3,6): #column
            if (copystate[i][j] == copystate[i+1][j-1]) & (copystate[i][j] == copystate[i+2][j-2]) & \
                    (copystate[i][j] == copystate[i+3][j-3]) & (copystate[i][j] != 'X'):
                return 1

    # Diaganol up-left
    for i in range(0, 4):  # row
        for j in range(0, 3):  # column
            if (copystate[i][j] == copystate[i + 1][j + 1]) & (copystate[i][j] == copystate[i + 2][j + 2]) & \
                    (copystate[i][j] == copystate[i + 3][j + 3]) & (copystate[i][j] != 'X'):
                return 1
    #tie
    if (validMoves(state) == []):
        return -1
    #not a goal state
    return 0

def userInputMakeMove(state,color):
    #Code will loop until a valid move is recieved

    #Print the board
    validInput = False
    while(validInput == False):
        printState(state)
        #print prompt and options
        print("You are: '" + color +"'")
        print("Possible Options: ")
        options = validMoves(state)
        print(options)
        choice = input("enter number of column (0-6) of desired move: ")

        #check fo a valid integer
        if (choice.isnumeric()):
            Inputchoice = int(choice)
            if ((Inputchoice < 7) & (Inputchoice >= 0) & (Inputchoice in options)):
                state = makeMove(state, Inputchoice, color)
                validInput = True

        if(validInput == False):
            print("ERROR: invlaid Entry")
            print("Try again. Input a number from 0-6 for desired column")
            print()
    return state



def playgame(algorithm1MakeMove, algorithm2MakeMove, verbose=False):
    #Plays the game with algorithm1 making the first move
    #Will return a 1 if algorithm1 ('R') wins,
    #a 2 if algorithm2 ('B') wins, or
    #a 0 if a tie is reached
    #Returns (winner,number of moves)
    #Verbose =True will display the game board for every move

    state = [[],[],[],[],[],[],[]]
    count = 0;
    while(validMoves(state) != []):
        #'R' goes first
        NewState = algorithm1MakeMove(state,'R')
        count = count + 1
        if (verbose):
            printState(state)
        if reachedGoalState(NewState) == 1:
            return 1, count
        elif reachedGoalState(NewState) == -1:
            return 0, count
        else:
            state = NewState
        #'B' goes second
        NewState = algorithm2MakeMove(state, 'B')
        count = count + 1
        if (verbose):
            printState(state)
        if reachedGoalState(NewState) == 1:
            return 2,count
        elif reachedGoalState(NewState) == -1:
            return 0,count
        else:
            state = NewState





def randomPlayerMakeMove(state,color):
    options = validMoves(state)
    choice = random.choice(options)

    state=makeMove(state, choice, color)
    return state

#print(reachedGoalState(state))
#options = validMoves(state)
#print(options)
#state = randomPlayerMakeMove(state,'R')
print(printState(state))
#print(playgame(randomPlayerMakeMove,randomPlayerMakeMove))
print(playgame(randomPlayerMakeMove,userInputMakeMove))