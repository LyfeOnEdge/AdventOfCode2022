CALORIE_LIST = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def find_max_calories(cal_list: str):
    # Parse list per elf
    return max(
        sum(int(cals) for cals in elf.split("\n")) for elf in cal_list.split("\n\n")
    )


print(find_max_calories(CALORIE_LIST))
