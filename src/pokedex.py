from pokemon import Pokemon


class Pokedex:

    def __init__(self, data):
        # Initialization of the class attributes , the arguments are values associated with theses keys in the Json object data
        self.pokemon_list:[Pokemon] = []
        for entry in data['pokemon']:
            pokemon = Pokemon(
            id=entry['id'],
            name=entry['name'],
            type=entry['type'],
            height=entry['height'],
            # Use of the get_weight method to convert weight which is a string in the data to a float
            weight=Pokemon.get_weight(entry['weight']),
            weaknesses=entry['weaknesses'],
            next_evolution=entry.get('next_evolution', []),
            prev_evolution=entry.get('prev_evolution', [])
        )
            self.pokemon_list.append(pokemon)

    def get_list_len(self) -> int:
        # count the number of pokemons objects
        return (len(self.pokemon_list))


    def get_heavier_than_ten(self) -> list:
        heavier_than_ten: list = []
        for pokemon in self.pokemon_list:
            if pokemon.weight > 10:
                heavier_than_ten.append(pokemon)
        return heavier_than_ten


    def sorted_by_weight(self):
        # use of a built in function to sort the list of dict
        return sorted(self.pokemon_list, key=lambda x: x.weight)

    def get_evolutions(self, pokemon_name: str):
        for pokemon in self.pokemon_list:
            # if a pokemon matches the name
            if pokemon.name == pokemon_name:
                # if there is a next evolution key for that pokemon
                if pokemon.next_evolution:
                    return pokemon.next_evolution
                else:
                    # if there is no evolutions for this given pokemon, print so
                    return f"{pokemon.name} does not have any evolution"
                return
        # if no pokemon matched the given name, print this message:
        return f"There is no pokemon called {pokemon_name}"


