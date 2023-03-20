class Animal:
    all = []
    def __init__(self, species, weight, nickname, daZoo ):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = daZoo
        Animal.all.append( self )

 # should take in an animal's species as an argument and return an list of 
    # all the animals, which are of that species

    @classmethod
    def find_by_species( cls, species):
        return [mate.nickname for mate in cls.all if mate.species == species]
