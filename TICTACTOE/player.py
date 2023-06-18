import random
import math

class Player:

      def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

      def get_sign(self):
        return self.sign

      def get_name(self):
        return self.name
     

      # for the players to choose a position on the board 
      def choose(self, board):
        while True:
            cell = input(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]:")
            if not board.isempty(cell):
                print("You did not choose correctly.")
                continue
            else:
                board.set(cell, self.sign)
                break

class AI(Player):
    def __init__(self, name, sign, board):
        super().__init__(name, sign)
        self.board = board
        
    # using random function to pick a choice from an available cell 
    def choose(self, board):
        available_cells = []
        for cell in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            if board.isempty(cell):
                available_cells.append(cell)
        cell = random.choice(available_cells)
        board.set(cell, self.sign)
    


class MiniMax(AI):
    def __init__(self, name, sign, board):
        super().__init__(name, sign, board)

    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)
    


    def minimax(self, board, self_player, start):
    # check the base conditions
        if board.isdone():
        # self is a winner
            if board.get_winner() == self.sign:
                return 1
        # is a tie
            elif board.get_winner() == "Tie":
                return 0
        # self is a looser (opponent is a winner)
            else:
                return -1
    
    # setting the minimum score
        if self_player:
            best_score = -math.inf
        else:
            best_score = math.inf
    
    # set the move 
        best_move = None
    
        for cell in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]:
            if board.isempty(cell):
                board.set(cell, self.sign if self_player else "O" if self.sign == "X" else "X")
            
            # call minimax recursively
                score = self.minimax(board, not self_player, False)
            
                board.set(cell, " ")
            
                if self_player:
                    if score > best_score:
                        best_score = score
                        best_move = cell
                else:
                    if score < best_score:
                        best_score = score
                        best_move = cell
                    
    # return the optimal move
        if start:
            return best_move
        else:
            return best_score
    


