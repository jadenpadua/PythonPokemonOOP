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

#Part 4, interaction between methods inside and outside a class
# Creds to @MaggieMao for this implementation
# Calculate damage index based on pokemon types
# Super effective = 2, not so effective = 0.5, normal = 1
def effectiveIndex(attacker, defender):
    # attacker and defender are passed in as two instances that we have created
  attackerType = attacker.pokeType
  defenderType = defender.pokeType
  # Water case for attacker
  if attackerType=='Water':
    if defenderType=='Fire':
      return 2
    elif defenderType=='Water':
      return 0.5
    else:
      return 1

  # Fire case for attacker
  elif attackerType=='Fire':
    if defenderType=='Grass':
      return 2
    if defenderType=='Water' or defenderType=='Electric':
      return 0.5
    else:
      return 1
  # Electric case for attacker
  elif attackerType=='Electric':
    if defenderType=='Water':
      return 2
    elif defenderType=='Electric':
      return 0.5
    else:
      return 1
  # Grass case for attacker
  elif attackerType=='Grass':
      if defenderType=='Water':
          return 2
      elif defenderType=='Electric':
        return 1
      else:
          return 0.5

#=========================================== 4
# Creds to @Maggie Mao for implementing this part :D

pokemon_1 = Pokemon('Fire', 12, 23, 33)
pokemon_2 = Pokemon('Water', 32, 32, 23)
print(effectiveIndex(pokemon_1, pokemon_2))
print(Pokemon.num_of_pokemons)