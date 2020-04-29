import random

import requests

import csv


## this is the start of the pokemon game logic
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


def run_pokemon_game():
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
        trump_choice = input(
            'Which statistic do you want to use? (id, height, weight, speed, special-defense, special-attack, defense, attack, hp)')

        while trump_choice not in ['id', 'height', 'weight', 'speed', 'special-defense', 'special-attack', 'defense',
                                   'attack', 'hp']:
            trump_choice = input(
                'You can only choose one of the statistics: id, height, weight, speed, special-defense, special-attack, defense, attack, hp. \n Try again!')

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
        print('Player 1 wins the game!!! CONGRATULATIONS!!!')
    elif player_1_score < player_2_score:
        print('Player 2 wins the game!!! CONGRATULATIONS!!!')
    else:
        print('Draw. Try again!')

    with open('pokemon_trump_scores.csv', 'a+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=['winner', 'trump choice', 'score'])
        spreadsheet.writerows(score)


## this is the end of the pokemon game logic

## this is the start of the harry potter game logic

def run_harrypotter_game():
    url = "http://hp-api.herokuapp.com/api/characters"
    response = requests.get(url)
    hp_characters = response.json()
    scoreList = []

    all_characters = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Draco Malfoy', 'Minerva McGonagall',
                      'Cedric Diggory', 'Cho Chang', 'Severus Snape', 'Rubeus Hagrid', 'Neville Longbottom',
                      'Luna Lovegood', 'Ginny Weasley', 'Sirius Black', 'Remus Lupin', 'Arthur Weasley',
                      'Bellatrix Lestrange', 'Lord Voldemort', 'Horace Slughorn', 'Kingsley Shacklebolt',
                      'Dolores Umbridge', 'Lucius Malfoy', 'Vincent Crabbe', 'Gregory Goyle', 'Mrs Norris',
                      'Argus Filch']

    # player_1 selection (human)
    print("Which character would you like to select?")
    print(all_characters)
    player_1_selection = input().title()
    player_char_dict = next(item for item in hp_characters if item["name"] == player_1_selection)
    # player_2 selection (computer)
    player_2_selection = random.choice(all_characters);
    computer_char_dict = next(item for item in hp_characters if item["name"] == player_2_selection)

    player_1 = {
        'name': player_char_dict['name'],
        'gender': player_char_dict['gender'],
        'house': player_char_dict['house'],
        'ancestry': player_char_dict['ancestry']
    }

    player_2 = {
        'name': computer_char_dict['name'],
        'gender': computer_char_dict['gender'],
        'house': computer_char_dict['house'],
        'ancestry': computer_char_dict['ancestry']
    }

    print("Player 1 selected: * {} *".format(player_1['name']))
    print("Player 2 was assigned: * {} *".format(player_2['name']))
    print(
        'Players earn points depending on their characters gender, house and ancestry - lets see what each player scored: \n')

    # player 1
    player_1_score = 0
    if player_1['gender'] == 'male':
        player_1_score += 5
    elif player_1['gender'] == 'female':
        player_1_score += 10

    if player_1['house'] == 'Gryffindor':
        player_1_score += 10
    elif player_1['house'] == 'Slytherin':
        player_1_score += 5
    elif player_1['house'] == 'Ravenclaw' or 'hufflepuff':
        player_1_score += 2

    if player_1['ancestry'] == 'pure-blood':
        player_1_score += 15
    elif player_1['ancestry'] == 'half-blood':
        player_1_score += 10
    elif player_1['ancestry'] == 'muggleborn':
        player_1_score += 5

    # player 2
    player_2_score = 0
    if player_2['gender'] == 'male':
        player_2_score += 5
    elif player_2['gender'] == 'female':
        player_2_score += 10

    if player_2['house'] == 'Gryffindor':
        player_2_score += 10
    elif player_2['house'] == 'Slytherin':
        player_2_score += 5
    elif player_2['house'] == 'Ravenclaw' or 'hufflepuff':
        player_2_score += 2

    if player_2['ancestry'] == 'pure-blood':
        player_2_score += 15
    elif player_2['ancestry'] == 'half-blood':
        player_2_score += 10
    elif player_2['ancestry'] == 'muggleborn':
        player_2_score += 5

    print('Player 1 scores: {}'.format(player_1_score))
    print('Player 2 scores: {}'.format(player_2_score))

    if player_1_score > player_2_score:
        print('\nPlayer 1 wins!!! CONGRATULATIONS human!!!')
        scoreList.append({'winner': 'Player1', 'Character': player_1['name'], 'score': player_1_score})

    elif player_1_score < player_2_score:
        print('\nPlayer 2 wins!!! CONGRATULATIONS computer!!!')
        scoreList.append({'winner': 'Player2', 'Character': player_2['name'], 'score': player_2_score})

    else:
        print('\nIts a draw - no one wins!')

    with open('HP_trump_scores.csv', 'a+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=['winner', 'Character', 'score'])
        spreadsheet.writerows(scoreList)

## this is the end of the harry potter game logic

## this is the logic to select which game the user wnats to play

pick_a_game = str(input("Which game do you want to play, Pokemon or Harry Potter? "))
if pick_a_game == "Pokemon" or pick_a_game == 'pokemon':
    run_pokemon_game()
elif pick_a_game == "harry potter" or pick_a_game == "Harry Potter":
    run_harrypotter_game()