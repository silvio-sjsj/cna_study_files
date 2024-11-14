""" .. """

class Player:

    def __init__(self, nom, pion):

        self.set_pion(pion)
        self.nom = nom

    def set_pion(self, symbole):

        self.__pion = symbole
    
    def get_pion(self):
        return self.__pion