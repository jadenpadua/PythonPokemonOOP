#Instatiate Pokemon class here with required params
class Pokemon:
    # Class variable of our total pokemon nummber
    num_of_pokemons = 0
    hp_boost = 1.08
    # dunder init is coverloaded constructor
    def __init__(self, pokeType,level,hp,attack):
        #sets the values of the instance to equal params passed in
        self.pokeType = pokeType
        self.level = level
        self.hp = hp
        self.attack = attack
        Pokemon.num_of_pokemons += 1
    # This is an instance Method in our class that displays full name
    def pokeStats(self):
        #Prints out to us all of our class attributes
        print("pokeType: " + self.pokeType)
        print("level: " + str(self.level))
        print("HP: " + str(self.hp))
        print("attack: " + str(self.attack))
    
    def health_boost(self):
        self.hp = int(self.hp * self.hp_boost)

pokemon_1 = Pokemon("fire",12,34,13)
print(pokemon_1.hp)
pokemon_1.health_boost()
print(pokemon_1.hp)