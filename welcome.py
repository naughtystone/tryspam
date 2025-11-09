#!/usr/bin/python

from kitchen import bacon, egg, lobster_thermidor, tomato, sausage
import random

INGREDIENTS = [egg.Egg(), bacon.Bacon(), LobsterThermidor, tomato, sausage.Sausage()]

def prepare_ingredient(ingredient):
    has_spam = random.choice([True,  False])
    return ingredient.prepare(has_spam)

def main():
    print('Scene: A cafe. A man and his wife enter.')
    print('Man: Well, what\'ve you got?')
    menu = []
    for ingredient in INGREDIENTS:
        menu.append(prepare_ingredient(ingredient))
    print('Waitress: Well, there\'s', ', '.join(menu))


if __name__ == '__main__':
    main()
