STRATEGY_GUIDE = """A Y
B X
C Z"""

points = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    },
    "X": 1,
    "Y": 2,
    "Z": 3,
}


def parse_guide(guide: str):
    total = 0
    for section in guide.split("\n"):
        shape, reaction = section.split()
        total += points[shape][reaction] + points[reaction]
    return total


print(parse_guide(STRATEGY_GUIDE))
