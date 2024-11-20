from typing import List, Optional

class Pokemon:
    def __init__(self, id: int, name: str, type: List[str], height: float, weight: float, weaknesses: List[str],
                 next_evolution: Optional[List[str]], prev_evolution: Optional[List[str]]):
        self.id = id
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight
        self.weaknesses = weaknesses
        self.next_evolution = next_evolution
        self.prev_evolution = prev_evolution

    def __repr__(self):
        return f"{self.name} (ID: {self.id}, Type: {self.type}, Weight: {self.weight}kg, Height: {self.height}, Next evolution: {self.next_evolution}, Previous evolution: {self.prev_evolution})"

    def get_weight(weight_str: str) -> float:
        # make a list that separates the words of the "weight" key originally composed of a number and "kg" after
        weight_str_list: list= weight_str.split(" ")
        # only keep the first item, so the number, and turn it into a float
        return float(weight_str_list[0])




