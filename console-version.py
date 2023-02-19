# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:29:29 2023

@author: simon
"""

#Battleships game in Python
#Rules
#10x10 grid with 4 ships (5,4,3,2)
#One grid with randomly assigned ships (computer_board)
#One grid where the player can place their own ships (player_board)
#Player can make a guess on computer_board. This is stored in a separate working board (computer_board_hits)
#Computer makes a guess on player_board. This is stored in a separate working board (player_board_hits)

#Game flow
#1print player_board
#2place_ships, store in player_board, print new version of player_board
#3place ships on computer_board (random assignment) but do not print
#4player guesses and creates an input with a number and a letter. Compare this input with computer_board.
#store result on player_guesses_board (which is initially an empty board but gets updated with each guess). Print player_guesses board.
#if hit repeat, if miss go on.
#5computer guesses and creates a random number and letter on the field which in its combination does not exist yet. Compare input with player_board.
#store result on computer_guesses_board (which is initally an empty board but gets updated with each guess). Print computer_guesses_board.
#if hit repeat, if miss go on.
#6alternate between player guesses and computer guesses until either player or computer scores all hits (=sum(length_of_ships)=17).


#init

import random
import numpy as np

length_of_ships = [2,3,4,5]
computer_board = [[0 for _ in range(10)] for _ in range(10)] #holds ships placed by computer
player_board = [[0 for _ in range(10)] for _ in range(10)] #holds ships placed by player
player_guesses_board = [[0 for _ in range(10)] for _ in range(10)] #holds guesses made by player
computer_guesses_board = [[0 for _ in range(10)] for _ in range(10)] #holds guesses made by computer

letters_to_numbers = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9}

target_mode = False
repetition = 0
computer_hits = []
computer_misses = []

potential_targets = []
target_direction = []
next_targets = []

cg_row = 9
cg_col = 9
cg_row_new = 0
cg_col_new = 0

#game

def print_board(board):
    if board == player_guesses_board or board == computer_guesses_board:
        display_board = np.copy(board)
        display_board[(display_board > 0) & (display_board < 9)] = 2
        display_board[display_board == 9] = 1
        for row in display_board:
            print(" ".join([str(cell) for cell in row]))
    else:
        for row in board:
            print(" ".join([str(cell) for cell in row]))

def place_ships(board):
    for ship_length in length_of_ships:
        while True:
            if board == computer_board:
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,9), random.randint(0,9)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = ship_length
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = ship_length
                        break
            else:
                place_ship = True
                print("Place the ship with a length of " + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):
                    if ship_overlaps(board, row, column, orientation, ship_length) == False:
                        if orientation == "H":
                            for i in range(column, column + ship_length):
                                board[row][i] = ship_length
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = ship_length
                        print_board(player_board)
                        break

def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 10:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 10:
            return False
        else:
            return True

def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "H":
        for i in range(column, column + ship_length):
            if board[row][i] != 0:
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] != 0:
                return True
    return False

def check_sunk(board):
    if board == player_guesses_board:
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == 2:
                    count2 += 1
                elif board[row][column] == 3:
                    count3 += 1
                elif board[row][column] == 4:
                    count4 += 1
                elif board[row][column] == 5:
                    count5 += 1
        if count2 == 2:
            print("You have sunk the ship with a length of 2")
        if count3 == 3:
            print("You have sunk the ship with a length of 3")
        if count4 == 4:
            print("You have sunk the ship with a length of 4")
        if count5 == 5:
            print("You have sunk the ship with a length of 5")

def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Enter orientation (H or V): ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print("Enter a valid orientation H or V")
        while True:
            try:
                row = input("Enter the row 1-10 of the ship: ")
                if row in "12345678910":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a valid letter between 1-10")
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in "ABCDEFGHIJ":
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-J")
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Enter the row 1-10 of the ship: ")
                if row in "12345678910":
                    row = int(row) - 1
                    break
            except ValueError:
                print("Enter a valid letter between 1-10")
        while True:
            try:
                column = input("Enter the column of the ship: ").upper()
                if column in "ABCDEFGHIJ":
                    column = letters_to_numbers[column]
                    break
            except KeyError:
                print("Enter a valid letter between A-J")
        return row, column

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column > 1 and column < 7:
                count += 1
    return count

def check_for_corner(target_direction):
    if target_direction[0] == 0 and target_direction[1] == 0:
        return True
    elif target_direction[0] == 9 and target_direction[1] == 0:
        return True
    elif target_direction[0] == 0 and target_direction[1] == 9:
        return True
    elif target_direction[0] == 9 and target_direction[1] == 9:
        return True
    else:
        return False

def check_for_border(target_direction):
    if target_direction[0] == 0:
        if computer_guesses_board[target_direction[0]+1][target_direction[1]] > 0 and \
            computer_guesses_board[target_direction[0]][target_direction[1]-1] > 0 and \
                computer_guesses_board[target_direction[0]][target_direction[1]+1] > 0:
            return True
    elif target_direction[0] == 9:
        if computer_guesses_board[target_direction[0]-1][target_direction[1]] > 1 and \
            computer_guesses_board[target_direction[0]][target_direction[1]-1] > 1 and \
                computer_guesses_board[target_direction[0]][target_direction[1]+1] > 1:
            return True
    if target_direction[1] == 0:
        if computer_guesses_board[target_direction[0]+1][target_direction[1]] > 1 and \
            computer_guesses_board[target_direction[0]-1][target_direction[1]] > 1 and \
                computer_guesses_board[target_direction[0]][target_direction[1]+1] > 1:
            return True
    elif target_direction[1] == 9:
        if computer_guesses_board[target_direction[0]+1][target_direction[1]] > 1 and \
            computer_guesses_board[target_direction[0]-1][target_direction[1]] > 1 and \
                computer_guesses_board[target_direction[0]][target_direction[1]-1] > 1:
            return True
    else:
        return False

def recode(row, col):
    if row < 0:
        row = 0
    elif row > 9:
        row = 9
    if col < 0:
        col = 0
    elif col > 9:
        col = 9
    return row, col

def turn(board):
    if board == player_guesses_board:
        row, column = user_input(player_guesses_board)
        if board[row][column] == 9:
            print("You already guessed this location, please try again.")
            turn(board)
        elif board[row][column] > 1:
            print("You have already guessed this location, please try again.")
            turn(board)
        elif computer_board[row][column] > 1:
            player_guesses_board[row][column] = computer_board[row][column]
        else:
            board[row][column] = 9
        return board
    else:
        global target_mode, computer_hits, computer_misses, repetition, target_direction, cg_row, cg_col, potential_targets
        if target_mode == False:
            cg_row = random.randint(0,9)
            cg_col = random.randint(0,9)
            if [cg_row, cg_col] in computer_hits or [cg_row, cg_col] in computer_misses:
                turn(board)
            elif player_board[cg_row][cg_col] > 1:
                board[cg_row][cg_col] = player_board[cg_row][cg_col]
                computer_hits.append([cg_row, cg_col])
                potential_targets = [(cg_row + 1, cg_col), (cg_row, cg_col + 1),
                                    (cg_row - 1, cg_col), (cg_row, cg_col - 1)]
                for row, col in potential_targets:
                    if (0 <= row <= 9) and \
                            (0 <= col <= 9) and \
                            (computer_board[row][col] == 0) and \
                            ((row, col) not in next_targets):
                        next_targets.append((row, col))
                target_mode = True
            elif player_board[cg_row][cg_col] == 0:
                board[cg_row][cg_col] = 9
                computer_misses.append([cg_row, cg_col])
        elif target_mode == True:
            target_direction = next_targets[0]
            next_targets.remove((target_direction[0], target_direction[1]))
            cg_row_new = target_direction[0]
            cg_col_new = target_direction[1]
            recode(cg_row_new, cg_col_new)
            if computer_guesses_board[cg_row_new][cg_col_new] != 0:
                if check_for_border(target_direction) == True or check_for_corner(target_direction) == True:
                    target_mode = False
                    turn(board)
                elif computer_guesses_board[cg_row][cg_col] != 0 and computer_guesses_board[cg_row][cg_col] != 0 and computer_guesses_board[cg_row][cg_col] != 0 and computer_guesses_board[cg_row][cg_col] != 0:
                    target_mode = False
                    turn(board)
            elif player_board[cg_row_new][cg_col_new] > 1:
                board[cg_row_new][cg_col_new] = player_board[cg_row_new][cg_col_new]
                computer_hits.append([cg_row_new, cg_col_new])
                potential_targets = [(cg_row_new + 1, cg_col_new), (cg_row_new, cg_col_new + 1),
                                    (cg_row_new - 1, cg_col_new), (cg_row_new, cg_col_new - 1)]
                for row, col in potential_targets:
                    if (0 <= row <= 9) and \
                            (0 <= col <= 9) and \
                            (computer_board[row][col] == 0) and \
                            ((row, col) not in next_targets):
                        next_targets.append((row, col))
                target_mode = True
            elif player_board[cg_row_new][cg_col_new] == 0:
                board[cg_row_new][cg_col_new] = 9
                computer_misses.append([cg_row_new, cg_col_new])
            return board

def play_game():
    place_ships(computer_board)
    #print("Enemy Board")
    #print_board(computer_board)
    print("Player Board")
    print_board(player_board)
    place_ships(player_board)
    while True:
        while True:
            print("Guess a battleship location")
            print("Enemy Board:")
            print_board(player_guesses_board)
            check_sunk(player_guesses_board)
            turn(player_guesses_board)
            break
        if count_hit_ships(player_guesses_board) == 14:
            print("You win")
            print_board(player_guesses_board)
            break
        #computer
        while True:
            turn(computer_guesses_board)
            break
        print("Computer Guesses:")
        print_board(computer_guesses_board)
        if count_hit_ships(computer_guesses_board) == 14:
            print("You loose")
            break

play_game()
