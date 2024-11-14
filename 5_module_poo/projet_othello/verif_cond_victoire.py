"""."""
from board import Board

class Verifier_la_condition_de_victoire(Board):

    def __init__(self, rows=6, columns=7):
        Board.__init__(self, rows=6, columns=7)
    
    def verifier_cond(self, grid, pion):

        for row in range(self.rows):
            for col in range(self.columns):
                if grid[row][col] == pion:
                    
                    # Checagem horizontal
                    if col + 3 < self.columns and all(grid[row][col+i] == pion for i in range(4)):
                        return True
                    
                    # checagem vertical
                    elif row + 3 < self.rows and all(grid[row+i][col] == pion for i in range(4)):
                        return True
                    
                    # checagem diagonal para a direita
                    elif row >= 3 and col+3 < self.columns and all(grid[row-i][col+i] == pion for i in range(4)):
                        return True
                    
                    # checagem diagonal para a esquerda
                    elif row >= 3 and col >= 3 and all(grid[row-i][col-i] == pion for i in range(4)):
                        return True
        
        return False