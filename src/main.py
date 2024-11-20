from pokedex import Pokedex
import json

# Opening the json file, reads it and converts it to a python object
with open('../data/pokedex.json', 'r', encoding='utf-8') as file:
    pokedex_data = json.load(file)

# Instanciation of the pokedex using the json file
pokedex = Pokedex(pokedex_data)

# calling and printing the methods
print(pokedex.get_list_len())
print(pokedex.get_heavier_than_ten())
print(pokedex.sorted_by_weight())

print("Eevee's next evolutions are:" , pokedex.get_evolutions("Eevee"))
print("Machamp's next evolutions are:" , pokedex.get_evolutions("Machamp"))
print("Bipboop's next evolutions are:" , pokedex.get_evolutions("Bipboop"))