#!/usr/bin/env python

# ---------------------------------------------------------
#
# Yet Another Tic Tac Toe program ;-)
#   tic tac toe with a test program and Gui
#
# ---------------------------------------------------------


# ---------------------------------------------------------
#
# Create a tictactoe board based on size and returns it
#
# ---------------------------------------------------------
def createBoard(size):
    board = []
    for rows in range(size):
        row = []
        for columns in range(size):
            row.append("-")
        board.append(row)
    return board

# ---------------------------------------------------------
#
# Print the tictactoe board to screen
#   will print board of any size
#
# ---------------------------------------------------------
def displayBoard(board):
    for row in board:
        print row

# ---------------------------------------------------------
#
# Checks if player has all consecutive cells in a
#   HORIZONTAL ROW. Will check all combinations regardless
#   of board size
#
# Returns true if there is at least one winning row, if
#   no winning rows, returns false
#
# ---------------------------------------------------------
def isHorizontalWin(board, player):
    winner = False
    consecutiveCells = 0
    numCellsNeededToWin = len(board)

    # check horizontal wins
    rowIndex = 0
    for row in board:
        columnIndex = 0
        for cell in row:
            if (board[rowIndex][columnIndex] == player):
                consecutiveCells = consecutiveCells + 1
            if (consecutiveCells == numCellsNeededToWin):
                winner = True
            columnIndex = columnIndex + 1
        rowIndex = rowIndex + 1
        consecutiveCells = 0
    return winner


# ---------------------------------------------------------
#
# Checks if player has all consecutive cells in a
#   VERTICAL COLUMN. Will check all combinations regardless
#   of board size
#
# Returns true if there is at least one winning COLUMN, if
#   no winning COLUMNS, returns false
#
# ---------------------------------------------------------
def isVerticalWin(board, player):
    winner = False
    consecutiveCells = 0
    numCellsNeededToWin = len(board)

    rowIndex = 0
    columnIndex = 0
    consecutiveCells = 0
    for columnIndex in range(len(board)):
        for rowIndex in range((len(board))):
            if (board[rowIndex][columnIndex] == player):
                consecutiveCells = consecutiveCells + 1
            if (consecutiveCells == numCellsNeededToWin):
                winner = True
        consecutiveCells = 0
    return winner


# ---------------------------------------------------------
#
# Checks if player has all consecutive cells in a
#   DIAGONAL. Will check all combinations regardless
#   of board size
#
# Returns true if there is at least one winning DIAGONAL, if
#   no winning DIAGONALS, returns false
#
# ---------------------------------------------------------
def isDiagonalWin(board, player):
    winner = False
    consecutiveCells = 0
    numCellsNeededToWin = len(board)

    rowIndex = 0
    columnIndex = 0
    consecutiveCells = 0
    for index in range(len(board)):
        if(board[rowIndex][columnIndex] == player):
            consecutiveCells += 1
        if (consecutiveCells == numCellsNeededToWin):
            winner = True
        rowIndex += 1
        columnIndex +=1

    rowIndex = 0
    columnIndex = len(board)-1
    consecutiveCells = 0
    for index in range(len(board)):
        if(board[rowIndex][columnIndex] == player):
            consecutiveCells += 1
        if (consecutiveCells == numCellsNeededToWin):
            winner = True
        rowIndex += 1
        columnIndex -=1
    return winner

# ---------------------------------------------------------
#
# Check if player won the game
#   will check all combinations regardless of board size
#
# ---------------------------------------------------------
def isWinner(board, player):
    if(isHorizontalWin(board,player) or isVerticalWin(board,player) or isDiagonalWin(board,player)):
        print("Player {} WINS".format(player))
        return True
    return False


# ---------------------------------------------------------
#
#  Flexible test framework that allows you to select
#    the size of the board, all methods will dynamically
#    scale up to the size of the board
#
# ---------------------------------------------------------

# set the test parameters
AUTOMATION_TEST_ENABLED = True
MAX_BOARD_SIZE = 3
PLAYER_ID = 'X'

if AUTOMATION_TEST_ENABLED == True:

    # create test matricies
    testBoards = []

    print("Start automated test")
    print("Each function will be unit tested")

    # dynamically create a board of size MAX_BOARD_SIZE
    print("Test: createBoard({})".format(MAX_BOARD_SIZE))
    board = createBoard(MAX_BOARD_SIZE)

    print("Test: displayBoard(board)")
    displayBoard(board)

    # create a 3x3 test boards and test all types of wins
    # test horizontal win 1
    print("Test: Horizontal Test 1")
    row1 = ['X', 'X', 'X']
    row2 = ['z', 'x', 'x']
    row3 = ['x', 'o', 'x']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # test horizontal win 2
    print("Test: Horizontal Test 2")
    row1 = ['X', 'X', 'o']
    row2 = ['X', 'X', 'X']
    row3 = ['x', 'o', 'x']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # test horizontal win 3
    print("Test: Horizontal Test 3")
    row1 = ['O', 'X', 'X']
    row2 = ['z', 'x', 'x']
    row3 = ['X', 'X', 'X']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # test vertical win 1
    print("Test: Vertical Test 1")
    row1 = ['X', 'o', 'x']
    row2 = ['X', 'x', 'O']
    row3 = ['X', 'o', 'x']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # test vertical win 2
    print("Test: Vertical Test 2")
    row1 = ['X', 'X', 'x']
    row2 = ['O', 'X', 'O']
    row3 = ['X', 'X', 'x']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # test vertical win 3
    print("Test: Vertical Test 3")
    row1 = ['X', 'o', 'X']
    row2 = ['o', 'x', 'X']
    row3 = ['X', 'o', 'X']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)


    # test diaganal win 1
    print("Test: Diagonal Test 1")
    row1 = ['X', 'o', 'X']
    row2 = ['o', 'X', 'o']
    row3 = ['X', 'o', 'X']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)


    # test diaganal win 2
    print("Test: Diagonal Test 2")
    row1 = ['X', 'o', 'X']
    row2 = ['o', 'X', 'o']
    row3 = ['X', 'o', 'X']
    gameBoard = [row1, row2, row3]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)


    # create a 4x4 test board and spot check win 1
    print("Test: 4x4 matrix Test 1")
    row1 = ['O', 'o', 'x', 'O']
    row2 = ['z', 'x', 'O', 'o']
    row3 = ['x', 'O', 'x', 'o']
    row4 = ['O', 'o', 'x', 'x']
    gameBoard = [row1, row2, row3, row4]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    # create a 4x4 test board and spot check win 2
    print("Test: 4x4 matrix Test 2")
    row1 = ['X', 'o', 'x', 'o']
    row2 = ['z', 'X', 'x', 'o']
    row3 = ['x', 'o', 'X', 'o']
    row4 = ['x', 'o', 'x', 'X']
    gameBoard = [row1, row2, row3, row4]
    testBoards.append(gameBoard)
    print("Test result: {} Player: {}".format(isWinner(gameBoard, PLAYER_ID),PLAYER_ID))
    displayBoard(gameBoard)

    print("End automated test")

else:
    print("Automation test DISABLED")

# -----------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------
#
# Yet Another Tic Tac Toe program
#   tic tac toe with a GUI (using tkinter framework)
#
# ---------------------------------------------------------

from tkinter import *
import tkinter.messagebox

# ---------------------------------------------------------
#
# Builds the data model of the board from the tkinter
#   GUI objects. Allows generic functions to be reused
#
# ---------------------------------------------------------

def buildModelFromButtons(buttons):
    gameBoardModel = [[0 for i in range(len(buttons))] for j in range(len(buttons))]
    for rowIndex in range(len(buttons)):
        for columnIndex in range(len(buttons)):
            gameBoardModel[rowIndex][columnIndex] = buttons[rowIndex][columnIndex]["text"]
            print("model: {}".format(buttons[rowIndex][columnIndex]["text"] ))
    return gameBoardModel

# ---------------------------------------------------------
#
# Disable user input after
#
# ---------------------------------------------------------

def disableButton():
    for rowIndex in range(boardSize):
        for columnIndex in range(boardSize):
            buttonMatrix[rowIndex][columnIndex].configure(state=DISABLED)

# ---------------------------------------------------------
#
# Callback function when buttons are clicked
#
# ---------------------------------------------------------

def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

# ---------------------------------------------------------
#
# Checks and displays win status
#
# ---------------------------------------------------------
def checkForWin():
    if isWinner(buildModelFromButtons(buttonMatrix), "O"):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif isWinner(buildModelFromButtons(buttonMatrix), "X"):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)

# ---------------------------------------------------------
#
# main program
#
# ---------------------------------------------------------

# get instance of the python GUI framework tkinter
tk = Tk()
tk.title("Ben's Awesome Tic Tac Toe Game")

# defined the game board size
boardSize = 3
buttonMatrix = [[0 for i in range(boardSize)] for j in range(boardSize)]

# program variables
pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
bclick = True
flag = 0
buttons = StringVar()

# add the player names
label = Label(tk, text="O - Player:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=boardSize+1, column=0)
label = Label(tk, text="X - Player:", font='Times 20 bold', bg='white', fg='black', height=1, width=8)
label.grid(row=boardSize+2, column=0)
player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=boardSize+1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=boardSize+2, column=1, columnspan=8)

# create the button widgets and dynamic game board
for rowIndex in range(boardSize):
    for columnIndex in range(boardSize):
        buttonMatrix[rowIndex][columnIndex] = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8,
           command=lambda rowIndex=rowIndex, columnIndex=columnIndex: btnClick(buttonMatrix[rowIndex][columnIndex]))
        buttonMatrix[rowIndex][columnIndex].grid(row=rowIndex, column=columnIndex)

# run the main program loop
tk.mainloop()
