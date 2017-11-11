import copy
state = [['R', 'B', 'R', 'B', 'R', 'B'], [], ['B'], [], [], [], []]

def printState(state):
    copystate = copy.deepcopy(state)
    for slot in copystate:
        slotlength = len(slot)
        for i in range(0, 6 - slotlength):
           slot.insert(0, 'X')

    for i in range(0, 6):
        for slot in copystate:
            print(slot[i] + ' '),
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
    for slot in state:
        if
        for space in slot:
