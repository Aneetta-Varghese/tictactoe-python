#tic tac toe game
#welcome
def welcome():
    print('welcome to the tic tac toe game').upper()
#board
board = [' ' for _ in range(9)]

def game():
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def assign(position,user):
    if board[position - 1]==' ':
        board[position - 1]=user
    else:
        print('position is already taken')
def check_winner():
    win_condition=[
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #row
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  #coloumn
        [0, 4, 8], [2, 4, 6]           #diagnoal
    ] 
    for i in win_condition:
        if board[i[0]]==board[i[1]]==board[i[2]] and board[i[0]]!=' ':
            return True
    return False
def draw():
    return '' not in board
def play():
    user1='X'
    user2='O'
    current_user=user1
    current_turn=1

    
    while True:
        game()
        while True:
            try:  
                position=int(input(f'player {current_turn} ({current_user}),choose your move(1-9): '))
                if 1 <= position <=9:
                    if board[position - 1]==' ':
                        assign(position,current_user)
                        break
                    else:
                        print('position already taken')
                else:
                    print('invalid input')
            except ValueError:
                print('Invalid input. Please enter a number.')
        if check_winner():
            game()       
            print(f' player {current_turn}({current_user}) won')
            break
        elif draw():
            game()
            print('draw')
            break
        current_user=user2  if current_user==user1 else user1
        current_turn=2 if current_turn==1 else 1

play()        
     