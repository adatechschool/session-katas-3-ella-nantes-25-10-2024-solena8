import json

# open the json file in read mode
with open("/home/solena/Ada/Exercices/Individuels/pokedex/data/pokedex.json", "r") as f:
    # parse and create a dictionary
    pokedex: dict = json.load(f)

print("type:",type(pokedex))
# print with indent to have a better visual representation of the dict
print(json.dumps(pokedex, indent=4))

# access the key "pokemon" (a list of dict) from the dict pokedex
pokemons: [dict] = pokedex["pokemon"]
# print(pokemons)

# count the number of pokemons objects aka nb of pokemons
print(len(pokemons))


# find out which pokemons weight more than 10kg :

def get_weight(weight_str: str) -> float:
    weight_str_list: list= weight_str.split(" ")
    return float(weight_str_list[0])

heavier_than_ten:list = []

for pokemon in pokemons:
    weight: float = get_weight(pokemon["weight"])
    if weight > 10:
        heavier_than_ten.append(pokemon["name"])

print(heavier_than_ten)

# Ecrire une fonction qui permet de les classer par ordre croissant de poids et afficher le résultat.

def display_sorted_by_weight(pokemon_list)-> [dict]:
    sorted_pokemons_by_weight:[dict] = sorted(pokemon_list, key=lambda x: get_weight(x['weight']))
    for pokemon in sorted_pokemons_by_weight:
        print(pokemon["name"], pokemon["weight"])

display_sorted_by_weight(pokemons)