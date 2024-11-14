"""
"""
from class_animal import Animal, Oiseau, Serpent

class Zoo:
    def __init__(self, animaux: list[Animal]):
        self.animaux = []

        for animal in animaux:
            self.put_animal_in_zoo(animal)

    def put_animal_in_zoo(self, animal: Animal):
        if isinstance(animal, Animal):
            self.animaux.append(animal)
        else:
            raise TypeError("Ce n'est pas un animal")
    
    def return_list_of_animals(self):
        return self.animaux
    
    def get_animals(self):
        for animal in self.animaux:
            print(f"Espèces: {animal.especes},\
                    Poids: {animal.poids},\
                    Taille: {animal.taille}")
    
    def __str__(self):
        msg = '-----------------------'
        msg += f"Ce zoo contient {len(self.animaux)} animaux"

        for animal in self.animaux:
            msg += f"\n{animal.especes}"
    
    def __add__(self, autre_zoo):
        return Zoo(self.animaux + autre_zoo.animaux)


if __name__ == "__main__":
    serpent = Serpent(5, 20, "anaconda")
    oiseau = Oiseau(2, 0.3, 50, "rossignol")
    zoo = Zoo([serpent, oiseau])
    #zoo.put_animal_in_zoo(oiseau)
    #zoo.put_animal_in_zoo(serpent)
    #zoo.return_list_of_animals()
    zoo.get_animals()
    print("---------------------------------")
    print("Création d'une nouvelle instance d'animal:")
    autre_serpent = Serpent(2, 11, "sucuri")
    zoo2 = Zoo([autre_serpent])
    zoo2.get_animals()
    print("---------------------------------")
    print("Ajouter les deux instances:")
    zoo = zoo + zoo2
    zoo.get_animals()