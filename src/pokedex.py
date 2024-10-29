import json

def get_db()->dict:
    # open the json file in read mode
    with open("../data/pokedex.json", "r") as f:
        # parse and create a dictionary
        pokedex: dict = json.load(f)
        return pokedex

print("type:",type(get_db()))
# print with indent to have a better visual representation of the dict
# print(json.dumps(get_db(), indent=4))


def get_pokemon_list(pokemon_list:list)-> list:
    if "pokemon" in pokemon_list:
        # access the key "pokemon" (a list of dict) from the dict pokedex
        pokemons: [dict] = pokemon_list["pokemon"]
        return pokemons
    else:
        print("there is no 'pokemon' key")
        return []

pokemon_list= get_pokemon_list(get_db())

def get_list_len(list)->int:
    # count the number of pokemons objects aka nb of pokemons
    return(len(list))

print(get_list_len(pokemon_list))

# find out which pokemons weight more than 10kg :

def get_weight(weight_str: str) -> float:
    # make a list that separates the words of the "weight" key originally composed of a number and "kg" after
    weight_str_list: list= weight_str.split(" ")
    # only keep the first item, so the number, and turn it into a float
    return float(weight_str_list[0])

def get_heavier_than_ten(pokemon_list)-> list:
    heavier_than_ten:list = []
    for pokemon in pokemon_list:
        # take the key "weight" from each pokemon object and use the function I created to
        # turn the string into a float
        weight: float = get_weight(pokemon["weight"])
        # if the weight is superior to 10, add it to the list
        if weight > 10:
            heavier_than_ten.append(pokemon["name"])
    return heavier_than_ten

print(get_heavier_than_ten(pokemon_list))


# write a function to sort by weight and display

def display_sorted_by_weight(pokemon_list):
    # use of a built in function to sort teh list of dict
    # using my functiont to get the weight as a float from a string
    sorted_pokemons_by_weight:[dict] = sorted(pokemon_list, key=lambda x: get_weight(x['weight']))
    for pokemon in sorted_pokemons_by_weight:
        print(pokemon["name"], pokemon["weight"])

display_sorted_by_weight(pokemon_list)


# a function to display the evolutions of a pokemon when given the name

def get_evolutions(pokemon_list :[dict], pokemon_name: str):
    for pokemon in pokemon_list:
        # if a pokemon matches the name
        if pokemon["name"] == pokemon_name:
            # if there is a next evolution key for that pokemon
            if "next_evolution" in pokemon:
                # get the next evolution name
                evolutions: [dict] = pokemon["next_evolution"]
                # make a string of each evolutions one after another and after an arrow
                evolutions_str = " -> ".join(evolution["name"] for evolution in evolutions)
                # print the name of the pokemon followed by all his evolutions
                print(f"{pokemon['name']} -> {evolutions_str}")
                return
            else:
                # if there is no evolutions for this given pokemon, print so
                print(f"{pokemon['name']} does not have any evolution")
                return
    # if no pokemon matched the given name, print this message:
    print(f"There is no pokemon called {pokemon_name}")


get_evolutions(pokemon_list, "Eevee")
get_evolutions(pokemon_list, "Machamp")
get_evolutions(pokemon_list, "bipboop")
