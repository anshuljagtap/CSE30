class Board:
    def __init__(self):
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            self.winner = ""
            

    def get_size(self): 
        return self.size

    def get_winner(self):
        return self.winner 

    def set(self, cell, sign):

        cell_index =  {"A1":0, "B1":1, "C1":2,
                      "A2": 3, "B2":4, "C2":5,
                      "A3": 6, "B3":7, "C3":8}[cell]
        self.board[cell_index] = sign
       
    #checking if the board is empty 
    def isempty(self, cell):
        cell =  {"A1":0, "B1":1, "C1":2,
                      "A2": 3, "B2":4, "C2":5,
                      "A3": 6, "B3":7, "C3":8}[cell] 
        return self.board[cell] == self.sign
         

    # conditions for results         
    def isdone(self):
            done = False
            winner = None
            winning_positions = [ [0, 1, 2], [3, 4, 5], [6, 7, 8],  # for rows
                                  [0, 3, 6], [1, 4, 7], [2, 5, 8],  # for columns
                                  [0, 4, 8], [2, 4, 6] ]# for diagonals
            
            for pos in winning_positions:
                if all(self.board[i] != self.sign and self.board[i] == self.board[pos[0]] for i in pos):
                    winner = self.board[pos[0]]
                    done = True
                    break

            if not done and self.sign not in self.board:
                done = True
                winner = "Tie"
                
                
                
                
             
            self.winner = winner
            return done

    #making the board according to the given format         
    def show(self):
        print("   A   B   C ")
        print(" +---+---+---+")
        for i in range(self.size):
            print(f"{i + 1}| {self.board[i * self.size]} | {self.board[i * self.size + 1]} | {self.board[i * self.size + 2]} |")
            print(" +---+---+---+")

