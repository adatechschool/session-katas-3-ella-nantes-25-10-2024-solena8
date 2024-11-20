# Pokédex Project

## Overview
This project is a Python-based Pokédex system developed as part of the Ada Tech School curriculum. It implements Object-Oriented Programming principles to manage and analyze Pokémon data from a JSON file, with features like weight-based sorting and evolution chain tracking.

## Features
- Load and parse Pokémon data from JSON
- Track Pokémon evolutions (both next and previous)
- Filter Pokémons by weight
- Sort Pokémons by weight
- Strong typing implementation using Python type hints

## Project Structure
```
project/
├── data/
│   └── pokedex.json    # Source data file
├── src/
│   ├── pokedex.py      # Main Pokédex class implementation
│   └── pokemon.py      # Pokemon class definition
    └── main.py             # Example usage and execution
```

## Classes

### Pokemon Class
Represents individual Pokémon with attributes:
- `id`: Unique identifier
- `name`: Pokémon name
- `type`: List of Pokémon types
- `height`: Height in meters
- `weight`: Weight in kg
- `weaknesses`: List of type weaknesses
- `next_evolution`: Optional list of next evolution names
- `prev_evolution`: Optional list of previous evolution names

### Pokedex Class
Manages the collection of Pokémon with methods:
- `get_list_len()`: Returns total number of Pokémon
- `get_heavier_than_ten()`: Returns list of Pokémon weighing more than 10kg
- `sorted_by_weight()`: Returns Pokémon list sorted by weight
- `get_evolutions(pokemon_name)`: Returns evolution information for a specific Pokémon

## Usage Example
```python
from pokedex import Pokedex
import json

# Load data from JSON file
with open('data/pokedex.json', 'r', encoding='utf-8') as file:
    pokedex_data = json.load(file)

# Create Pokedex instance
pokedex = Pokedex(pokedex_data)

# Get total number of Pokémon
print(pokedex.get_list_len())

# Get Pokémon heavier than 10kg
heavy_pokemon = pokedex.get_heavier_than_ten()

# Get sorted list by weight
sorted_pokemon = pokedex.sorted_by_weight()

# Check evolution chain
print(pokedex.get_evolutions("Eevee"))
```

## Technical Implementation Details
- Uses Python's type hints for better code reliability
- Implements custom `__repr__` method for readable Pokémon representation
- Handles optional evolution chains using `Optional` type
- Includes weight conversion from string format (e.g., "10.0 kg") to float

## Installation
1. Clone this repository:
```bash
git clone [your-repository-url]
cd pokedex
```

2. Ensure you have Python 3.x installed
3. Place your `pokedex.json` file in the `data` directory

## Data Format
The project expects a JSON file with the following structure:
```json
{
  "pokemon": [
    {
      "id": 1,
      "name": "Example",
      "type": ["Type1", "Type2"],
      "height": "0.7 m",
      "weight": "6.9 kg",
      "weaknesses": ["Type1", "Type2"],
      "next_evolution": ["Evolution1"],
      "prev_evolution": ["Evolution1"]
    }
  ]
}
```

## Contributing
This is a school project for Ada Tech School. While it's not open for contributions, feedback and suggestions are welcome.

## License
This project is part of Ada Tech School curriculum. All rights reserved.

## Acknowledgments
- Ada Tech School for the project requirements and guidance
- Pokémon data provided as part of the course material
