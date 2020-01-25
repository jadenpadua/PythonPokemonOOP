#Instatiate Pokemon class here with required params
class Pokemon:
    # dunder init is coverloaded constructor
    def __init__(self, pokeType,level,hp,attack):
        #sets the values of the instance to equal params passed in
        self.pokeType = pokeType
        self.level = level
        self.hp = hp
        self.attack = attack
    
    # This is an instance Method in our class that displays full name
    def pokeStats(self):
        #Prints out to us all of our class attributes
        print("pokeType: " + self.pokeType)
        print("level: " + str(self.level))
        print("HP: " + str(self.hp))
        print("attack: " + str(self.attack))
#Creation of our General pokemon objects
pokemon_1 = Pokemon('Fire',12,47,13)
pokemon_2 = Pokemon('Water', 23,68,57)
pokemon_3 = Pokemon('Electric',73,89,90)

# Now accessing our object values
print(pokemon_1.__dict__)
print(pokemon_2.__dict__)
print(pokemon_3.__dict__)
print('===========')
# Invoking our pokeStats methods
pokemon_1.pokeStats()
print('===========')
pokemon_2.pokeStats()
print('===========')
pokemon_3.pokeStats()