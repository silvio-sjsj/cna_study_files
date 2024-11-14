""" ...
"""

class Animal:

    def __init__(self, poids, taille):

        self.poids = poids
        self.taille = taille
    
    def se_deplacer(self):
        print("Every type of animal moves in a different way")

class Serpent(Animal):

    def __init__(self, poids, taille,  especes):

        Animal.__init__(self, poids, taille)
        self.especes = especes
    
    def serpent_attr(self):

        print(f"This is a serpent of type {self.especes}, taille {self.taille} and poids {self.poids}")

    def se_deplacer(self):
        print("Je rampe")

class Oiseau(Animal):

    def __init__(self, poids, taille, altitude_max, especes):

        super().__init__(poids, taille)
        self.altitude_max = altitude_max
        self.especes = especes

    def se_deplacer(self):
        print("Je vole")
"""
if __name__ == "__main__":

    serpent = Serpent(5, 20, "anaconda")
    oiseau = Oiseau(2, 0.3, 50, "rossignol")
"""