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
# Now our electric type class will inherit our Pokemon superclass
class ElectricType(Pokemon):
    # new hp boost, we can change class methods within subclass and will override
    hp_boost = 1.30
    # now we can init
    def __init__(self, pokeType,level,hp,attack,electricAbility):
        # notice that we can inherit the properities from the superclass and not have to set setters again
        super().__init__(pokeType,level,hp,attack)
        # for unique functionalities specific to electric type
        self.electricAbility = electricAbility

      # Boosts hp of our pokemon
    def health_boost(self):
        self.hp = int(self.hp * self.hp_boost + 45)
# Now nesting objects Pokemon -> ElectricType -> Pikachu
class Pikachu(ElectricType):
    hp_boost = 2.40
    # init constuctor inherits from Electric type which inherits from pokemon
    def __init__(self, pokeType,level,hp,attack,electricAbility,name,specialAbility):
        super().__init__(pokeType,level,hp,attack,electricAbility)
        self.name = name
        self.specialAbility = specialAbility  
    # Call instance method that uses special ability here
    def useSpecialAbility(self):
        print("Pikachu used " +self.specialAbility + "!")
    
# Poke Trainer that has a list of Pokemon 
class PokeTrainer:
    # same init logic from before
    def __init__(self, name, level, hp, attack, pokedex = None):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        # can add conditional logic to constructor
        if pokedex is None:
            self.pokedex = []
        # case where pokemon already initialized into our pokedex
        else:
            self.pokedex = pokedex

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokedex:
            self.pokedex.append(pokemon)

    def remove_pokemon(self, pokemon):
        if pokemon in self.pokedex:
            self.pokedex.remove(pokemon)
    
    def print_pokedex(self):
        for pokemon in self.pokedex:
            print('==>',pokemon)




def effectiveIndex(attacker, defender):
    # attacker and defender are passed in as two instances that we have created
  attackerType = attacker.pokeType
  defenderType = defender.pokeType
  # Water case for attacker
  if attackerType=='Water':
    if defenderType=='Fire':
      return 2
    elif defenderType=='Water' or defenderType=='Grass':
      return 0.5
    else:
      return 1

  # Fire case for attacker
  elif attackerType=='Fire':
    if defenderType=='Grass':
      return 2
    if defenderType=='Water':
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

#=========================================== 5
pikachu_1 = Pikachu('Electric',34,45,56,"Thunderbolt","Pikachu","Static")
trainer_dave = PokeTrainer('Dave',12,24,34,[])
print(trainer_dave.__dict__)
trainer_dave.add_pokemon(pikachu_1.name)
print(trainer_dave.__dict__)
trainer_dave.remove_pokemon(pikachu_1.name)
print(trainer_dave.__dict__)
trainer_dave.add_pokemon(pikachu_1.name)
print(trainer_dave.print_pokedex())
