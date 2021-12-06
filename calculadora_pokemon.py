
import  random
import math


class Pokemon:
    
    def __init__(self, name, level, attack, defense, power):
        self.name = name
        self.level = level
        self.attack = attack
        self.defense = defense
        self.power = power

    def damage(self, other_pokemon):
            target = 1
            weather = 1
            badge = 1
            critical = 1 
            numero_random = random.uniform(0.85, 1)
            STAB = 1
            type = 1
            burn = 1
            other = 1
            damage = math.floor(((((((2*other_pokemon.level)/5)+2)*other_pokemon.power*(other_pokemon.attack/self.defense))/50)+2)*target*weather*badge*critical*numero_random*STAB*type*burn*other)
        
            return damage




if __name__ == '__main__':
    
    #Pokemones de ejemplo
    pokemon_attacking = Pokemon("Glaceon", 75, 123, 10, 65)
    pokemon_defending = Pokemon("Garchomp", 10, 10, 163, 1)

    print("{} vs {}".format(pokemon_attacking.name, pokemon_defending.name))
    print("Battle!")
    print("{}'s damage is {}".format(pokemon_defending.name, pokemon_defending.damage(pokemon_attacking)))




