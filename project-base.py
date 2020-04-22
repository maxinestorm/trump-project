import random

import requests


def select_random_pokemon():
    pokemon_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

# print(select_random_pokemon()['name'])

def run():
    player_1 = select_random_pokemon()

    print('Player 1 was given {}'.format(player_1['name']))
    trump_choice = input('Which trump do you want to use? (id, height, weight) ')

    player_2 = select_random_pokemon()
    print('Player 2 was given{}'.format(player_2['name']))

    player_1_trump_choice = player_1[trump_choice]
    player_2_trump_choice = player_2[trump_choice]

    if player_1_trump_choice < player_2_trump_choice:
        print('Player 2 WINS!!!')
    elif player_1_trump_choice > player_2_trump_choice:
        print('Player 1 WINS!!!')
    else:
        print('No one wins this round')


run()

hello everyone
