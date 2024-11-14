import random
from board import Board
from players import Player
from verif_cond_victoire import Verifier_la_condition_de_victoire

class Game:

    def __init__(self):
        self.board = Board()
        self.players = [
            Player("Player 1", 'O'),
            Player("Player 2", 'X')
        ]
        self.i = random.choice(range(0, 2))
        self.verifier = Verifier_la_condition_de_victoire()

    def choose_a_move(self):
        
        print("        START OF THE GAME           ")
        print("       _____________________        ")

        while True:
            
            grid = self.board.afficher_plateau()
            #self.board.verifier_colonnes_disponibles(grid)

            current_player = self.players[self.i]
            print("#####################################################")
            print(f"{current_player.nom}'s turn")
            pion = current_player.get_pion()

            disponibles = self.board.verifier_colonnes_disponibles(grid)

            while True:
                try:
                    column = int(input("Choose a column between the available ones: ")) 

                    if column in disponibles:
                        grid = self.board.ajouter_un_pion(column, pion)
                        break
                    else:
                        print("Invalid column! Chose between the available ones")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6.")

            # check win condition
            if self.verifier.verifier_cond(grid, pion):
                grid = self.board.afficher_plateau()
                print(f"{current_player.nom} wins!")
                break
            
            if len(disponibles) == 0:
                print("   ----- A PARTIDA TERMINOU EMPATADA ----- ")
                break

            self.switch_turns()

    def switch_turns(self):
        current_player = self.i

        if self.i == 1:
            self.i = 0
        else:
            self.i = 1
        
    def check_win_condition():
        raise NotImplementedError

if __name__ == "__main__":
    game = Game()
    game.choose_a_move()
    