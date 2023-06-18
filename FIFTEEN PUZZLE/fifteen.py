#Author: Anshul Jagtap



import numpy as np
from random import choice

class Fifteen:
    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array([i for i in range(1, size**2)] + [0])
        self.adj = [self.get_adjacent(i) for i in range(size**2)]
        
    def get_adjacent(self, index):
        adj = []
        if index % self.size > 0:
            adj.append(index-1)         # left
        if index % self.size < self.size-1:
            adj.append(index+1)         # right
        if index // self.size > 0:
            adj.append(index-self.size) # up
        if index // self.size < self.size-1:
            adj.append(index+self.size) # down
        return adj


    def update(self, move):
        #Slide the tile numbered `move` into the empty space if it's a valid move.
        if self.is_valid_move(move):
            index = np.where(self.tiles == move)[0][0]
            empty_index = np.where(self.tiles == 0)[0][0]
            self.tiles[index], self.tiles[empty_index] = self.tiles[empty_index], self.tiles[index]

    def transpose(self, i, j):
        #Swap rows `i` and `j` and columns `i` and `j` of the board.
        self.tiles = self.tiles.reshape((self.size, self.size))
        self.tiles[:, [i, j]] = self.tiles[:, [j, i]]
        self.tiles[[i, j], :] = self.tiles[[j, i], :]
        self.tiles = self.tiles.flatten()

    def shuffle(self, steps=100):
        #Randomly shuffle the tiles by sliding a random tile into the empty space `steps` number of times.
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        #heck if the tile numbered `move` can be slid into the empty space.
        if move not in self.tiles:
            return False
        move_index = np.where(self.tiles == move)[0][0]
        empty_index = np.where(self.tiles == 0)[0][0]
        return move_index in self.adj[empty_index]

    def is_solved(self):
        solved_state = np.array([i for i in range(1, self.size**2)] + [0])
        return np.array_equal(self.tiles, solved_state)


    def draw(self):
        for i in range(self.size):
            print("+---" * self.size + "+")
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                if tile == 0:
                    tile_str = "   "
                else:
                    tile_str = "{:2d} ".format(tile)
                print("|" + tile_str, end="")
            print("|")
        print("+---" * self.size + "+")

    def __str__(self):
    # Initialize an empty string to store the output
        output = ''
    # Iterate over each row of the puzzle
        for i in range(self.size):
        # Iterate over each column of the puzzle
            for j in range(self.size):
                index = i * self.size + j
           
                tile = self.tiles[index]
                if tile != 0:
                    output += f"{tile:2d} "
                else:
                    output +="   "
            output += '\n'
        # Return the output string
        return output



if __name__ == '__main__':
    
    game = Fifteen()
    game.draw()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    print(str(game))
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''
    '''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
    '''
