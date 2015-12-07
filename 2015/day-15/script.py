#!/usr/bin/env python

import re

def parse_line(line):
    m = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
    return ( int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6)) )

def teaspoon(quantity, ingredient):
    return tuple(map(lambda x: x * quantity, ingredient))

def combine(ingredient_1, ingredient_2):
    if ingredient_1 is None:
        return ingredient_2

    return tuple(x + y for x, y in zip(ingredient_1, ingredient_2))

def compute_score(combination, verif_calories):
    if (combination is None):
        return 0

    if verif_calories and combination[-1] != 500:
        return 0

    res = 1
    for i in range(len(combination) - 1):
        value = combination[i]
        res *= value if value > 0 else 0

    return res

def find_optimal_recipe(ingredients, remaining_teaspoons, combination = None, verif_calories = False):
    if (not ingredients) or (remaining_teaspoons == 0):
        return compute_score(combination, verif_calories)

    remaining_ingredients = ingredients.copy()
    ingredient = remaining_ingredients.pop()

    optimal_score = 0
    for i in range(remaining_teaspoons + 1):

        score = find_optimal_recipe(
            remaining_ingredients,
            remaining_teaspoons - i,
            combine(combination, teaspoon(i, ingredient)),
            verif_calories)

        if score > optimal_score:
            optimal_score = score

    return optimal_score

if __name__ == '__main__':

    set_of_ingredients = set()
    
    f = open('data')
    for line in f:
        set_of_ingredients.add(parse_line(line))
    f.close()

    print('[Part 1] Optimal score is:', find_optimal_recipe(set_of_ingredients, 100))
    print('[Part 2] Optimal score is:', find_optimal_recipe(set_of_ingredients, 100, verif_calories = True))
