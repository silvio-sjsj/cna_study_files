"""
Classe Board: représente l'état et la gestion du plateau de jeu
"""
class Board:

    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.grid = [[" " for _ in range(columns)] for _ in range(rows)]

    def afficher_plateau(self):
        
        print("  0  "+" 1  "+" 2  "+" 3  "+" 4  "+" 5  "+" 6  ")
        for row in self.grid:
            print("| " + " | ".join(row) + " |")
            print("-" * (4 * self.columns + 2))
        
        return self.grid
    
    def ajouter_un_pion(self, column, pion):
        
        for row in range(len(self.grid))[::-1]:
            if self.grid[row][column] == ' ':
                self.grid[row][column] = pion
                break
    
        return self.grid
    
    def verifier_colonnes_disponibles(self, grid):

        collones_disponibles = []

        for col in range(self.columns):
            for row in range(len(grid))[::-1]:
                if grid[row][col] == ' ':
                    collones_disponibles.append(col)
                else:
                    pass
        
        collones_disponibles = set(collones_disponibles)
        print(f"The following colmuns are available {collones_disponibles}")
        return collones_disponibles
    
    def verifier_is_full(self, grid):
        raise NotImplementedError