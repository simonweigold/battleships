# battleships

#Rules
10x10 grid with 4 ships (5,4,3,2)
One grid with randomly assigned ships (computer_board)
One grid where the player can place their own ships (player_board)
Player can make a guess on computer_board. This is stored in a separate working board (computer_board_hits)
Computer makes a guess on player_board. This is stored in a separate working board (player_board_hits)

#Game flow
1. print player_board
2. place_ships, store in player_board, print new version of player_board
3. place ships on computer_board (random assignment) but do not print
4. player guesses and creates an input with a number and a letter. Compare this input with computer_board.
store result on player_guesses_board (which is initially an empty board but gets updated with each guess). Print player_guesses board.
if hit repeat, if miss go on.
5. computer guesses and creates a random number and letter on the field which in its combination does not exist yet. Compare input with player_board.
store result on computer_guesses_board (which is initally an empty board but gets updated with each guess). Print computer_guesses_board.
if hit repeat, if miss go on.
6. alternate between player guesses and computer guesses until either player or computer scores all hits (=sum(length_of_ships)=17).

The first version allows gameplay within the console. Next steps include adding a user interface (Pygame would work for that) and improving the AI.
