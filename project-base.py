import random

import requests

import csv

def select_random_HP_House():
    potter_house = random.randint()
    url= 'http://hp-api.herokuapp.com/api/characters/'.format(potter_house)
    response = requests.get(url)
    HP_House = response.json()

    HP_dicts = {
        'house': HP_House['house'],
        'name': HP_House['name'],
        'ancestry': HP_House['ancestry'],
        'gender': HP_House['gender'],
        'alive': HP_House['alive'],
    }

    return HP_dicts

def run():

def select_random_pokemon():
    pokemon_id = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()

    stat_dicts = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }

    for stat in pokemon['stats']:
        stat_name = stat['stat']['name']
        stat_value = stat['base_stat']
        stat_dicts[stat_name] = stat_value

    return stat_dicts

def run():
    player_1_score = 0
    player_2_score = 0
    score = []
    for i in range(5):
        player_1 = select_random_pokemon()

        print('Player 1 was given {}, id: {}, height: {}, weight: {}, \n speed: {}, special-defense: {},'
              ' special-attack: {}, defense: {}, attack: {}, hp: {}'.format(
                    player_1['name'], player_1['id'], player_1['height'], player_1['weight'], player_1['speed'],
                    player_1['special-defense'], player_1['special-attack'], player_1['defense'], player_1['attack'],
                    player_1['hp']))
        trump_choice = input('Which trump do you want to use? (id, height, weight, speed, special-defense, special-attack, defense, attack, hp)')

        while trump_choice not in ['id', 'height', 'weight', 'speed', 'special-defense', 'special-attack', 'defense', 'attack', 'hp']:
            trump_choice = input('You can only choose one of the trumps: id, height, weight, speed, special-defense, special-attack, defense, attack, hp. \n Try again!')

        player_2 = select_random_pokemon()
        print('Player 2 was given {}, id: {}, height: {}, weight: {}, \n speed: {}, special-defense: {},'
              ' special-attack: {}, defense: {}, attack: {}, hp: {}'.format(
                player_2['name'], player_2['id'], player_2['height'], player_2['weight'], player_2['speed'],
                player_2['special-defense'], player_2['special-attack'], player_2['defense'], player_2['attack'],
                player_2['hp']))

        player_1_trump_choice = player_1[trump_choice]
        player_2_trump_choice = player_2[trump_choice]

        if player_1_trump_choice < player_2_trump_choice:
            print('Player 2 wins a round!')
            player_2_score += 1
            score.append({'winner': 'Player2', 'trump choice': trump_choice, 'score': player_2_trump_choice})

        elif player_1_trump_choice > player_2_trump_choice:
            print('Player 1 wins a round!')
            player_1_score += 1
            score.append({'winner': 'Player1', 'trump choice': trump_choice, 'score': player_1_trump_choice})
        else:
            print('No one wins this round')

        print()

    print('Player 1 won {} rounds'.format(player_1_score))
    print('Player 2 won {} rounds'.format(player_2_score))

    if player_1_score > player_2_score:
        print('Player 1 won a game!!! CONGRATULATIONS!!!')
    elif player_1_score < player_2_score:
        print('Player 2 won a game!!! CONGRATULATIONS!!!')
    else:
        print('Draw. Try again!')

    with open('trump_scores.csv', 'a+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=['winner', 'trump choice', 'score'])
        spreadsheet.writerows(score)

pick_a_game=str(input("Which Game do you want to play,Pokemon or harry potter?"))
if pick_a_game == "pokemon":
    select_random_pokemon()
elif pick_a_game == "harry potter":
    select_random_HP_House()

run()