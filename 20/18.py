import re


class IntPartOne(int):
    def __sub__(self, other):
        return self.__class__(super().__mul__(other))

    def __add__(self, other):
        return self.__class__(super().__add__(other))


class IntPartTwo(int):
    def __mul__(self, other):
        return self.__class__(super().__add__(other))

    def __add__(self, other):
        return self.__class__(super().__mul__(other))


def eval_line_part_one(line):
    return eval(
        re.sub(r"(\d+)", r"IntPartOne(\1)", line.translate(str.maketrans("*", "-")))
    )


def eval_line_part_two(line):
    return eval(
        re.sub(r"(\d+)", r"IntPartTwo(\1)", line.translate(str.maketrans("+*", "*+")))
    )


lines = open("18.txt").readlines()
print(sum(map(eval_line_part_one, lines)))
print(sum(map(eval_line_part_two, lines)))
