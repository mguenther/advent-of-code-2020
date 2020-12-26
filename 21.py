from collections import defaultdict
from typing import Dict, List, Tuple

import pprint
import sys


def parse(filename: str) -> Tuple[Dict[int, Dict], Dict[str, List[int]]]:
    
    raw_lines = [l.strip().replace('(', '').replace(')', '') for l in open(filename, 'r').readlines()]
    recipes = {}
    allergences_to_recipes = defaultdict(lambda: [])
    allergences_to_possible_ingredients = defaultdict(lambda: [])

    for i, recipe in enumerate(raw_lines):
        ingredients, supplemental = recipe.split('contains')
        ingredients = set([i.strip() for i in ingredients.split(' ') if i != ''])
        allergenes = set([allergene.strip() for allergene in supplemental.split(',')])
        recipes[i] = {
            'ingredients' : ingredients,
            'allergenes' : allergenes
        }
        for allergene in allergenes:
            allergences_to_recipes[allergene].append(i)
            allergences_to_possible_ingredients[allergene] += ingredients
    
    return recipes, allergences_to_recipes, allergences_to_possible_ingredients


recipes, allergences_to_recipes, allergences_to_possible_ingredients = parse('21.in')
F = []

while len(allergences_to_recipes) > 0:
    found = False
    found_allergene = None
    for allergene in allergences_to_recipes:
        S = set(allergences_to_possible_ingredients[allergene])
        for recipe in allergences_to_recipes[allergene]:
            S = S.intersection(recipes[recipe]['ingredients'])
        if len(S) == 1:
            ingredient = S.pop()
            print("Ingredient " + ingredient + " contains " + allergene + ".")
            for recipe in recipes:
                if ingredient in recipes[recipe]['ingredients']:
                    print("\t\t\tRemoving ingredient " + ingredient + " from recipe " + str(recipe) + ".")
                    recipes[recipe]['ingredients'].remove(ingredient)
                if allergene in recipes[recipe]['allergenes']:
                    print("\t\t\tRemoving allergene " + allergene + " from recipe " + str(recipe) + ".")
                    recipes[recipe]['allergenes'].remove(allergene)
            found = True
            found_allergene = allergene
            F.append((allergene, ingredient))
            break
    if found:
        del allergences_to_recipes[allergene]
    
res = 0
for recipe in recipes:
    res += len(recipes[recipe]['ingredients'])
print("Solution to part one: " + str(res))

F.sort()
print("Solution to part two: " + ','.join([i[1] for i in F]))