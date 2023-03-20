from lib.animal import Animal

class Zoo:
    all = []
    def __init__( self, name, location):
        self.name = name 
        self.location =location 
        Zoo.all.append( self )

# should return all the animals that a specific instance of a zoo has.

    @property
    def animals( self ):
        newInDaZoo = []
        for mate in Animal.all:
            newInDaZoo.append( mate )
        return newInDaZoo
    
# should return an list of all the species (as strings) of 
    # the animals in the zoo. However, if you have two dogs, it should only 
    # return one "Dog" string (aka an unique list).

    @property
    def animal_species( self ):
        return list( { mate.species for mate in self.animals })
    
 # should take in an animal's species as an argument and return an list of 
    # all the animals in that zoo, which are of that species.

    
    def find_by_species( self, species ):
        return [mate for mate in self.animals if mate.species == species]
    

 # should return an list of all the nicknames of animals that a specific 
    # instance of a zoo has.


    @property
    def animal_nicknames( self ):
        return [ mate.nickname for mate in self.animals ]
    
    
  # should take in a location as an argument and return an list of all the 
    # zoos within that location.
    
    @classmethod
    def find_by_location( cls, daLocation):
        return [ z for z in cls.all if z.location == daLocation ]

