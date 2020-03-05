def print_board(board):

    print('\n')
    print(f"\t{board[6]} | {board[7]} | {board[8]}\n\t--|---|--\n\t{board[3]} | {board[4]} | {board[5]}\n\t--|---|--\n\t{board[0]} | {board[1]} | {board[2]}")
    print('\n')
    pass

def player_choice():
    char = input('Player1 choose your symbol: (X or O) ')

    while char.upper() != 'X' and char.upper() != 'O' :
        char = input('invalid input! Try again: ')

    return char.upper()

def place_marker(board,marker,position):

    if board[position-1] == ' ':
        board[position-1]=marker
        return False
    else:
        print("The selected space is alredy full, please choose another one!")
        return True

def check_win(board, symbol):
    if board[0:3] == [symbol,symbol,symbol] or board[3:6] == [symbol,symbol,symbol] or board[6:9] == [symbol,symbol,symbol]:
        return True
    elif board[0:7:3] == [symbol,symbol,symbol] or board[1:8:3] == [symbol,symbol,symbol] or board[2:9:3] == [symbol,symbol,symbol]:
        return True
    elif board[0] == symbol == board[4] == board[8]:
        return True
    elif board[2] == symbol == board[4] == board[6]:
        return True

    return False

def board_full(board):
    for num in range(0,len(board)):
        if board[num] == ' ': return False

    return True

if __name__ == "__main__":
    import os

    #printing board
    my_board =[' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print("TicTacToe, let's play!")
    print_board([1,2,3,4,5,6,7,8,9])

    #symbol assignment
    player1 = player_choice()
    player2 = ''

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    
    
    winner = ''

    while(not board_full(my_board)):

        num = int(input("Player 1 make your move: "))
        while place_marker(my_board,player1,num):
            num = int(input("Player 1 make your move: "))
        if check_win(my_board,player1) :
            winner = player1
            break
        os.system('cls')
        print_board(my_board)
        if board_full(my_board): break

        num = int(input("Player 2 make your move: "))
        while place_marker(my_board,player2,num):
            num = int(input("Player 2 make your move: "))
        if check_win(my_board,player2) :
            winner = player2
            break
        os.system('cls')
        print_board(my_board)
            

    if len(winner) != 0:
        print('The winner is '+ winner)
    else:
        print("Draw!")

    pass