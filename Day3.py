import string

CONTENTS = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

priority_map = {}
for i, char in enumerate([*string.ascii_lowercase, *string.ascii_uppercase]):
    priority_map[char] = i + 1


def parse_contents(contents: str) -> list:
    sacks = []
    for line in contents.split("\n"):
        half = len(line) // 2
        sacks.append(([c for c in line[:half]], [c for c in line[half:]]))
    return sacks


def calculate_priorities(contents: str) -> int:
    total = 0
    for sack in parse_contents(contents):
        # Find uniques
        sack_a, sack_b = set(sack[0]), set(sack[1])
        for c in sack_a:
            if c in sack_b:
                total += priority_map[c]
                break
    return total


print(calculate_priorities(CONTENTS))
