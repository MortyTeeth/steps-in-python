import sys


def for_sell():
    data = [pokemon.strip() for pokemon in sys.stdin]
    dict_with_pokemons = dict()
    counter = 0

    for pokemon in data:
        if pokemon not in dict_with_pokemons:
            dict_with_pokemons.update({pokemon: 1})
        else:
            counter += 1
    return counter


print(for_sell())
