from typing import Dict, List, Tuple, Union


number = Union[float, int]


def maximum(nameScores: List[Tuple[str, number]]) -> Tuple[str, number]:
    return max(nameScores, key=lambda nameScore: nameScore[1])
