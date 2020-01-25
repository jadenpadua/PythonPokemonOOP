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
    # Boosts hp of our pokemon
    def health_boost(self):
        self.hp = int(self.hp * self.hp_boost)
    # Class method changes hp_boost for all instances of pokemon class
    @classmethod
    def change_hp_boost(cls, amount):
        cls.hp_boost = amount
    
    @classmethod
    def convertPokeString(cls,poke_str):
        #Parse poke string passed in
        pokeType, level, hp, attack = poke_str.split('-')
        return cls(pokeType, level, hp, attack) #now make new pokemon object in constructor  

    @staticmethod
    # Pokemon will recover on the weekends
    def is_Recovering(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False    

# =========================================== 3
pokemon_1 = Pokemon("fire",12,34,13)
print(pokemon_1.hp)
pokemon_1.health_boost()
print(pokemon_1.hp)
pokemon_1.change_hp_boost(2)
pokemon_1.health_boost()
print(pokemon_1.hp)

poke_string_1 = Pokemon.convertPokeString("Water-18-23-65")
print(poke_string_1.__dict__)

import datetime
current_date = datetime.date(2020,1,19)
print(Pokemon.is_Recovering(current_date))
# =========================================== 4
