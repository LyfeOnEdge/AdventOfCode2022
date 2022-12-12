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


def parse_guide(guide: str) -> int:
    total = 0
    for section in guide.split("\n"):
        shape, reaction = section.split()
        total += points[shape][reaction] + points[reaction]
    return total


if __name__ == "__main__":
    with open("Day2_input.txt") as f:
        guide = f.read().strip()
    print(parse_guide(guide))
