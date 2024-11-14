""" ...
"""

class Animal:

    def __init__(self, poids, taille):

        self.set_poids(poids)
        self.taille = taille

    def get_poids(self):
        return self.__poids
    
    def set_poids(self, animal_poids):

        if animal_poids > 0:
            self.__poids = animal_poids
        else:
            raise ValueError(f"Poids doit être > 0")
    
    def se_deplacer(self):
        print("Every type of animal moves in a different way")

class Serpent(Animal):

    def __init__(self, poids, taille,  type):

        Animal.__init__(self, poids, taille)
        self.type = type
    
    def serpent_attr(self):

        print(f"This is a serpent of type {self.type}, taille {self.taille} and poids {self.poids}")

    def se_deplacer(self):
        print("Je rampe")

class Oiseau(Animal):

    def __init__(self, poids, taille, altitude_max, type):

        super().__init__(poids, taille)
        self.altitude_max = altitude_max
        self.type = type

    def se_deplacer(self):
        print("Je vole")