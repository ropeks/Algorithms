#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  ingredients_left = True
  batches_num = -1

  while ingredients_left:
        batches_num += 1
        for i in recipe:
              if i in ingredients.keys():
                   if recipe[i] <= ingredients[i]:
                         ingredients[i] -= recipe[i]
                   else:
                         ingredients_left = False
                         break
        return batches_num



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))