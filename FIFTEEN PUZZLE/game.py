#author: Anshul Jagtap


from tkinter import *
import random

class Fifteen:
    def __init__(self, master):
        self.master = master
        self.master.title("Fifteen Puzzle")

        self.tiles = []
        self.empty_tile = None
        self.font = ("Helvetica", 20, "bold")

        self.create_board()
        self.shuffle()

    def create_board(self):
        # Create tiles in the correct order
        for i in range(1, 16):
            tile = Button(self.master, text=str(i), font=self.font, width=4, height=2)
            tile.grid(row=(i-1)//4, column=(i-1)%4)
            tile.bind("<Button-1>", self.move_tile)
            self.tiles.append(tile)

        # Create empty tile
        self.empty_tile = Button(self.master, text="", font=self.font, width=4, height=2, state=DISABLED, bg="gray")
        self.empty_tile.grid(row=3, column=3)

        # Add tiles to the board
        for i, tile in enumerate(self.tiles):
            tile.grid(row=i//4, column=i%4)

# shuffling the puzzle
    def shuffle(self):
        random.shuffle(self.tiles)
        for i, tile in enumerate(self.tiles):
            tile.grid(row=i//4, column=i%4)
        self.tiles.append(self.empty_tile)

    def move_tile(self, event):
        tile = event.widget
        tile_row, tile_col = tile.grid_info()["row"], tile.grid_info()["column"]
        empty_row, empty_col = self.empty_tile.grid_info()["row"], self.empty_tile.grid_info()["column"]
        if (tile_row == empty_row and abs(tile_col-empty_col) == 1) or (tile_col == empty_col and abs(tile_row-empty_row) == 1):
            tile.grid(row=empty_row, column=empty_col)
            self.empty_tile.grid(row=tile_row, column=tile_col)
            self.tiles[self.tiles.index(tile)], self.tiles[-1] = self.tiles[-1], tile

if __name__ == "__main__":
    root = Tk()
    Fifteen(root)
    root.mainloop()
