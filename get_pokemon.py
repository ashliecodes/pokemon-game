# Pokemon Top Trumps

# importing modules
import requests
import random

from pprint import pprint  # pretty print


def random_pokemon(pokemon_number):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(
        pokemon_number)  # url to pokemon API formatted as the pokemon number
    response = requests.get(url)  # makes request to web page
    pokemon = response.json()  # returns a JSON object of the result

    pokemon_name = pokemon['name']

    return (pokemon_name)


def pokemon_hp(pokemon_name):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_name)
    response = requests.get(url)  # makes request to web page
    pokemon = response.json()

    hp = pokemon['base_experience']

    return (hp)


def pokemon_moves(name):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(name)
    response = requests.get(url)  # makes request to web page
    pokemon = response.json()  # returns a JSON object of the result

    pokemon_moveset = []
    moves = pokemon['moves']
    for move in moves:
        pokemon_moveset.append(move['move']['name'])

    return (pokemon_moveset)


def call_move_power(move_name):
    url = 'https://pokeapi.co/api/v2/move/{}/'.format(move_name)
    response = requests.get(url)
    pokemon = response.json()

    power = pokemon['power']

    return (power)


def make_move_dictionary(pokemon_name):
    pokemon_move_list = pokemon_moves(
        pokemon_name)  # adds all the pokemon moves to one long list, calls on the pokemon_move function to do this
    # print(pokemon_move_list)

    number_of_moves = len(pokemon_move_list)  # variable for how many moves a pokemon has.

    # For Loop that pick four battle moves at random from the list in the API and displays them to the player.
    random_moves = []  # defines a list for the 4 random moves to be put into

    # for moves in range(4):
    while len(random_moves) < 4:
        random_number_choice = random.randint(0, (number_of_moves - 1))
        chosen_move = pokemon_move_list[random_number_choice]
        chosen_move_power = call_move_power(chosen_move)
        if chosen_move_power == None:
            continue
        else:
            random_moves.append(chosen_move)



    # print(random_moves)
    pokemon_move_power = {}

    # assigns both the move and the move's power to a dictionary using the move power function above
    for i in range(len(random_moves)):
        # print(random_moves[i])
        pokemon_move_power[random_moves[i]] = call_move_power(random_moves[i])  # calls on the call_move_power function to get the values, adds it to a dictionary

    return (pokemon_move_power)


def BATTLE_FUNCTION(player_pkmn, opponent_pkmn, player_hp, opponent_hp, player_moves, opponent_moves):
    # PLAYER STATS
    player_pkmn_hp = player_hp
    opponent_pkmn_hp = opponent_hp

    while player_pkmn_hp > 0 and opponent_pkmn_hp > 0:

        stat_choice = input('Choose your battle move! (Please type it exactly as it appears above.) ')
        print('you selected {}'.format(stat_choice))

        opponent_random_move_choice = random.choice(list(opponent_moves.items()))
        opponent_move_value = opponent_random_move_choice[1]

        player_move = 0
        if stat_choice in [key for key in player_moves.keys()]:
            player_move = player_moves[stat_choice]  # ASSIGNS THE DICTIONARY VALUE OF THE CHOSEN MOVE TO A VARIABLE
        else:
            print("error! A random move has been chosen for you.")
            player_random_move_choice = random.choice(list(player_moves.items()))
            player_move = player_random_move_choice[1]
            print("You selected {}".format(player_random_move_choice[0]))

        print("")
        print("The move " + stat_choice + " does a damage total of: " + str(player_move))
        print("The opponent's move " + opponent_random_move_choice[0] + " does a damage total of: " + str(
            opponent_move_value))
        # COMPARE STATS
        print("")

        randomlist = [0, 0, 0, 1]
        n = random.randint(0, 3)
        random_number = randomlist[n]
        #print("random number for randomlist:  " + str(random_number))

        if player_move > opponent_move_value:
            print("Your chosen move is more powerful than the opponent's move!")
            if random_number == 0:
                 print("You attacked the enemy " + opponent_pkmn + ".")
                 print(str(player_move) + " damage dealt!")
                 opponent_pkmn_hp -= player_move
            elif n == 1:
                print("Your attack failed")

        elif opponent_move_value > player_move:
            print("The opponent's move is more powerful than your chosen move!")
            if random_number == 0:
                print("The enemy " + opponent_pkmn + " attacked your " + player_pkmn + ".")
                print(str(opponent_move_value) + " damage dealt!")
                player_pkmn_hp -= opponent_move_value
            elif random_number == 1:
                print("The opponent's attack failed")


        print("")
        print("Player's Pokemon " + player_pkmn + " has " + str(player_pkmn_hp) + " HP remaining.")
        print("Enemy Pokemon " + opponent_pkmn + " has " + str(opponent_pkmn_hp) + " HP remaining.")

        print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
        print("")

    if player_pkmn_hp <= 0:
        print("Your Pokemon HP has dropped below 0!")
        print("Oh no, Team Rocket won this round!")
        return (0)  # 0 means opponent won
    elif opponent_pkmn_hp <= 0:
        print("The opponent Pokemon's HP has dropped below 0!")
        print("Congratulation you defeated Team Rocket!")
        return (1)  # 1 means player won


number_of_times_to_repeat = 3
p = 0

player_score = 0
opponent_score = 0

while p < number_of_times_to_repeat:

    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("PLAYER POKEMON INFORMATION")
    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("")

    player_pokemon = random_pokemon(random.randint(1, 151))
    player_pokemon_hp = pokemon_hp(player_pokemon)

    print(player_pokemon + " // HP: " + str(player_pokemon_hp))
    print(player_pokemon + "'s moves:")

    player_pokemon_moves = make_move_dictionary(player_pokemon)

    for i in range(len(player_pokemon_moves)):
        print("MOVE NAME: " + [key for key in player_pokemon_moves.keys()][i] + " ; POWER: " + str(
            [value for value in player_pokemon_moves.values()][i]))

    ##DEFINE OPPONENT POKEMON

    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("OPPONENT POKEMON INFORMATION")
    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("")

    opponent_pokemon = random_pokemon(random.randint(1, 151))
    opponent_pokemon_hp = pokemon_hp(opponent_pokemon)
    print(opponent_pokemon + " // HP: " + str(opponent_pokemon_hp))
    opponent_pokemon_moves = make_move_dictionary(opponent_pokemon)

    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("WHICH MOVE WILL YOU CHOOSE?")
    print("=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=")
    print("")

    score = BATTLE_FUNCTION(player_pokemon, opponent_pokemon, player_pokemon_hp, opponent_pokemon_hp,
                            player_pokemon_moves, opponent_pokemon_moves)


    if score == 0:
        opponent_score += 1
    elif score == 1:
        player_score += 1

    print("Your score: " + str(player_score))
    print("Enemy score: " + str(opponent_score))
    p += 1



if player_score < opponent_score:
    print("Your score: " + str(player_score))
    print("Enemy score: " +str(opponent_score))
    print("Oh no, you lose the game!! Team Rocket won!!!!!")
elif player_score > opponent_score:
    print("Your score: " + str(player_score))
    print("Enemy score: " + str(opponent_score))
    print("Congratulation you defeated Team Rocket! You won the game!!")
elif player_score == opponent_score:
    print("It's a tie!")