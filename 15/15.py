import collections
import itertools
import math
import re

max_ingredients = 100

ingredients = {
    name: tuple(map(int, re.findall(r"-?\d+", properties)))
    for name, properties in (line.split(":") for line in open("15.txt"))
}

recipe_property_scores = set(
    tuple(
        max(
            0,
            sum(
                properties[i] * recipe[name] for name, properties in ingredients.items()
            ),
        )
        for i in range(5)
    )
    for recipe in map(
        collections.Counter,
        itertools.combinations_with_replacement(ingredients, max_ingredients),
    )
)

# part 1
print(max(math.prod(scores[:4]) for scores in recipe_property_scores))

# part 2
print(
    max(
        math.prod(scores[:4])
        for scores in filter(lambda scores: scores[4] == 500, recipe_property_scores)
    )
)
