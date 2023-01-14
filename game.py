import math
import random
import time
class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all player to get their next move given a game
    def get_move(self, game):
        pass
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        value_square = False
        val = None
        while not value_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            # here we will also check that this is a correct value by trying to cast it 
            # if to integer, and it's not, then we say its invalid
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                value_square = True #if these are succesful
            except ValueError:
                print("Invalid square. Try again.")
        return val
class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #randomly chooses one
        else:
            # get the square based off the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    def minimax(self, state , player):
        max_player = self.letter
        other_player = "O" if player == "X" else "X" # other player
        # first we want to check if the previous move is a winner 
        # this is our base case
        if state.current_winner == other_player:
            # we should return position AND score because we need to keep track of the score
            # for minmax to work
            return {'position': None,
                    'score': 1*state.num_empty_squares() + 1 if other_player == max_player else -1*(state.num_empty_squares()+1)}
        elif not state.empty_squares(): # no empty squares
                return {'position': None, 'score':0}
        if player == max_player:
            best = {'postion' : None, 'score': -math.inf } # each score should maximise so be larger
        else:
            best = {'postion' : None, 'score': math.inf }
        for possible_move in state.available_moves():
            # step 1: make a move, try that spot
            state.make_move(possible_move,player)
            # step 2: recurse using minmax to sumulate a game after making that move
            sim_score = self.minimax(state,other_player) # now we alternate player
            # step 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move # otherwise this will messed up from the recursion

            # step 4: update the dictionaries
            if player == max_player:
               if sim_score['score'] > best ['score']:
                   best = sim_score # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score # replace best
        return best

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




        

