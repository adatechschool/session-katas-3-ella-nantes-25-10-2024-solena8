import pandas as pd
import json

pd.set_option('display.max_columns', None)  # Affiche toutes les colonnes
pd.set_option('display.max_rows', None)     # Affiche toutes les lignes
pd.set_option('display.width', 1000)

def get_db() -> dict:
    # Ouvre le fichier JSON en mode lecture
    with open("../data/pokedex.json", "r") as f:
        # Parse et crée un dictionnaire
        pokedex: dict = json.load(f)
        return pokedex

def get_pokemon_list(pokemon_list: dict) -> list:
    if "pokemon" in pokemon_list:
        # Accède à la clé "pokemon" (une liste de dictionnaires) du dictionnaire pokedex
        pokemons: [dict] = pokemon_list["pokemon"]
        return pokemons
    else:
        print("Il n'y a pas de clé 'pokemon'")
        return []

# Obtenons la liste des Pokémon et construisons le DataFrame
pokemon_list = get_pokemon_list(get_db())
df = pd.DataFrame(pokemon_list)

# Transformation de la colonne `weight` en float
df["weight"] = (
    df["weight"]
    .str.replace(" kg", "", regex=False)  # Enlève " kg"
    .astype(float)                        # Convertit en float
)

# Filtre les Pokémon lourds (> 10 kg)
heavy_pokemons = df[df["weight"] > 10]
heavy_pokemons_sorted_by_name= heavy_pokemons.sort_values(by="name")

df_sorted_by_name = df.sort_values(by="name")

# print(heavy_pokemons[["id", "name", "weight"]])

# Filtrer pour trouver les évolutions de Eevee

def get_evolutions(name: str, database: pd.DataFrame):
    # Vérifie si le nom du Pokémon existe dans le DataFrame
    if (database["name"] == name).any():
        # Récupère les évolutions du Pokémon
        pokemon_evolutions = database[database["name"] == name]["next_evolution"].values[0]

        # Vérifie si pokemon_evolutions est bien une liste
        if isinstance(pokemon_evolutions, list) and len(pokemon_evolutions) > 0:
            print(f"Évolutions de {name}:")
            for evolution in pokemon_evolutions:
                print(f" -> {evolution['name']}")
        else:
            print(f"{name} n'a pas d'évolutions.")
    else:
        print(f"{name} n'existe pas dans la base de données.")


# Exemple d'appels de la fonction
get_evolutions("Eevee", df)
get_evolutions("ploup", df)
get_evolutions("Machamp", df)

