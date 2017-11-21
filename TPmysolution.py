import copy
state = [['R', 'B', 'R', 'B', 'R', 'B'], [], ['B'], [], [], [], []]

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
    state[move].insert(0, color)

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
    #not a goal state
    return 0
