def move(board):
    def indtotuple(combinedboard, c):
        # finds index tuple of first space occupied by c on board (c can be ' ', 'T', or 'U')
        return (combinedboard.index(c)//3, combinedboard.index(c)%3)

    def blockorwin(combboard, win = False):
        combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        if win:
            for i in combos:
                line = ''.join([combboard[i[0]], combboard[i[1]], combboard[i[2]]])
                if line.count('U') == 2:
                    if ' ' in line:
                        return (i[line.index(' ')]//3, i[line.index(' ')]%3)
            return None
        else:
            for i in combos:
                line = ''.join([combboard[i[0]], combboard[i[1]], combboard[i[2]]])
                if line.count('T') == 2:
                    if ' ' in line:
                        return (i[line.index(' ')]//3, i[line.index(' ')]%3)
            for i in combos:
                line = ''.join([combboard[i[0]], combboard[i[1]], combboard[i[2]]])
                if line.count(' ') == 2 and line.count('U') == 1:
                    return (i[line.index(' ')]//3, i[line.index(' ')]%3)
            return indtotuple(combboard, ' ')
    
    combined = ''.join([''.join(i) for i in board])
    nospace = [i for i in combined if i != ' ']
    turn = len(nospace) + 1
    if turn % 2 == 1:
        if turn == 1:
            return (0,0)
        if turn == 3:
            nextmove = {1:(2,0), 2: (2,0), 3:(0,2), 4:(2,2), 5:(0,2), 6:(0,2), 7:(2,0), 8:(0,2)}
            oppmove1ind = combined.index('T')
            return nextmove[oppmove1ind]
        if turn == 5:
            if blockorwin(combined, True) != None:
                return blockorwin(combined, True)
            else:
                if combined[4] == 'T':
                    if combined[2] == 'T':
                        return (2,0)
                    elif combined[6] == 'T':
                        return (0,2)
                    else:
                        return blockorwin(combined)
                elif combined[8] == 'U':
                    return (0,2)
                elif combined[8] == 'T':
                    if combined[2] == 'U':
                        return (2,0)
                    else:
                        return (0,2)
                elif combined[2] == 'T' or combined[6] == 'T':
                    return (2,2)
                else:
                    return (1,1)
        if turn == 7:
            if combined[4] == 'T':
                if combined[2] == 'U':
                    if combined[1] == 'T':
                        return (1, 2)
                    else:
                        return (0, 1)
                else:
                    if blockorwin(combined, True) != None:
                        return blockorwin(combined, True)
                    else:
                        return blockorwin(combined)
            else:
                return blockorwin(combined, True)
        if turn == 9:
            return indtotuple(combined, ' ')
            
    else:
        if turn == 2:
            if board[1][1] == ' ':
                return (1,1)
            else:
                return (0,0)
        else:
            if blockorwin(combined, True) == None:
                return blockorwin(combined)
            else:
                return blockorwin(combined, True)
    

#CODE BELOW CREATED BY GT CS TESTER

#Below is some code that will run your agent. Specifically,
#this code has your agent play against itself, as both X and
#O. X will move first. The version of the game board fed into
#your move() function will still use U and T, but it will be
#shown in the output as X and O so that it makes sense to read.
#Checks if anyone has won the game yet. Returns a tuple whose
#first value is a boolean representing whether the game is
#over and whose second value is a string representing the result.
def game_result(board):
    #Check horizontal winner
    #Check row 0
    if board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check row 1
    if board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        if not board[1][0] == " ":
            return True, board[1][0]
    #Check row 2
    if board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        if not board[2][0] == " ":
            return True, board[2][0]
    #Check column 0
    if board[0][0] == board[1][0] and board[0][0] == board[2][0]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check column 1
    if board[0][1] == board[1][1] and board[0][1] == board[2][1]:
        if not board[0][1] == " ":
            return True, board[0][1]
    #Check column 2
    if board[0][2] == board[1][2] and board[0][2] == board[2][2]:
        if not board[0][2] == " ":
            return True, board[0][2]
    #Check top-left to bottom-right diagonal
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if not board[0][0] == " ":
            return True, board[0][0]
    #Check bottom-left to top-right diagonal
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if not board[0][2] == " ":
            return True, board[0][2]
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False, "Continue"
    return True, "Draw"

#Changes a game from Xs and Os to Us and Ts depending on whose
#move it is.
def pivot_board(board, player):
    pivoted_board = [["?","?","?"],["?","?","?"],["?","?","?"]]
    if player == "X":
        replacement_dictionary = {" ": " ", "X": "U", "O": "T"}
    else:
        replacement_dictionary = {" ": " ", "X": "T", "O": "U"}
    for i in range(3):
        for j in range(3):
            pivoted_board[i][j] = replacement_dictionary[board[i][j]]
    return pivoted_board

#Print the game board to the console.
def print_board(board):
    print("{0}|{1}|{2}\n-----\n{3}|{4}|{5}\n-----\n{6}|{7}|{8}\n".format(board[0][0], board[0][1], board[0][2],
                                                                     board[1][0], board[1][1], board[1][2],
                                                                     board[2][0], board[2][1], board[2][2]))


#Main game-running engine.
def test_game():
    game_board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    current_player = "X"
    game_done = False

    while not game_done:
        print(current_player + "'s turn...")

        #Gets next move based on the current board, pivoting it
        #to show the player's own moves as U and the opponent's
        #as T.
        result = move(pivot_board(game_board, current_player))

        #Checks if result is a tuple with two items, and prints
        #INVALID MOVE if not. Quits the game if the move is not
        #valid.
        try:
            row, column = result
        except:
            print("INVALID MOVE:", result)
            break

        #Checks if the move is legal, e.g. consists of two integers
        #in range and is not a move on top of an existing move.
        #Prints INVALID MOVE if not. Quits the game if the move
        #is not valid.
        try:
            if not game_board[row][column] == " ":
                print("INVALID MOVE:", row, column)
                break

            #Updates the game board if the move appeared valid.
            game_board[row][column] = current_player
        except:
            print("INVALID MOVE:", row, column)
            break

        #Changes the current player.
        current_player = "O" if current_player == "X" else "X"

        #Prints the current board.
        print_board(game_board)

        #Checks if the game has a winner or is a draw.
        game_done, winner = game_result(game_board)

    #Prints the final result if the game finished completely
    #(no invalid moves).
    if game_done:
        if winner == "Draw":
            print("It's a draw!")
        else:
            print(winner, "wins!")

if __name__ == '__main__':
    test_game()
