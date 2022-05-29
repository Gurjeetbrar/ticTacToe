from tic_tac_toe import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
import time
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use single list to rep 3X3 board
        self.current_winner = None # keep track of winner
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' | '.join(row)+ ' |')
    @staticmethod
    def print_board_nums():
        # 0 1 2 etc (tells) us what number correspond to which box
        number_board = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| '+' | '.join(row)+ ' |')
    def available_moves(self):
        # return []
        # easy way to write
        return [i for i,spot in enumerate(self.board) if spot == ' ']
        # for (i,spot) in enumerate(self.board):
        #     # ['x' , 'x' , 'o' ] --> [(0,'x'),(1,'x'),(2,'o')]
        #     if spot == ' ':
        #         moves.append(i)
       
    def empty_squares(self):
        return ' ' in self.board
    def num_empty_squares(self):
        return self.board.count(" ")
    def make_move(self, square, letter):
        #if valid move, then make the move (assign square to letter)
        # then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square, letter):
        #winner if 3 in row anywhere.. we have to check all the these
        row_idx = square//3
        row = self.board[row_idx*3:(row_idx + 1)*3]
        if all([spot == letter for spot in row]):
            return True
        # check column
        col_idx = square%3
        col = [self.board[col_idx+i*3] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True
        #check diagonal
        if square%2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]  
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal1 ]) or all([spot == letter for spot in diagonal2 ]):
                return True
        return False

def play(game, x_player, o_player,print_game = True):
    #return the winner of the game! or None for tie
    if print_game:
        game.print_board_nums()
    letter = 'X' #starting letter
    # iterate while the game still has empty square
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # let's define a function to make move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print('')  #just empty line
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == "X" else "X" #switches player
            #tiny pause 
            time.sleep(0.9)
    if print_game :
        print("It's a tie")  
if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t,x_player,o_player, print_game = True)




        

