from itertools import combinations, permutations

import numpy as np
import pandas as pd

from score_hand import score_my_hand

#create deck by iterating over 2 lists

def create_deck():
    deck = []
    suits = ['D', 'C', 'H', 'S']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for value in values:
            deck.append(f'{value}{suit}')
        # print(deck)
    return deck

#function to create matrix of 7 card combination and score each possibility
# it will then reorder the matrix with the best hand at the top
def get_winning_player_combinations(player_1_np, remaining_cards_combinations_np):
    player_1_np_dimension = np.expand_dims(player_1_np, axis=0)

    player_1_np_repeat = np.repeat(
        a=player_1_np_dimension, repeats=len(remaining_cards_combinations_np), axis=0)

    all_combinations = np.hstack((player_1_np_repeat, remaining_cards_combinations_np))

    all_scores = np.apply_along_axis(score_my_hand, 1, all_combinations)

    # turn 1-d vector into 2d-matrix for concatenation
    all_scores = all_scores.reshape(-1, 1)

    # use dtype 'O' because otherwise ints in all_scores get turned to strings
    all_combinations_with_scores = np.concatenate(
        (all_combinations, all_scores), axis=1, dtype='O')

    # sort descending by last column (7)-hack to do descending not ascending
    #cheat method from stack overflow
    return all_combinations_with_scores[all_combinations_with_scores[:,7].argsort()[::-1]]

#this is main function that was asked for in brief
def make_the_winner(players_csv_file, first_three_community_cards, winner):
    #import csv file and create deck
    players_df = pd.read_csv(players_csv_file)
    print(players_df)
    deck = create_deck()
    #remove community cards from deck
    for card in first_three_community_cards:
        deck.remove(card)
    #create a dictionary called players and iterate over csv whilst also removing cards from deck
    #each player should end up with 5 cards (2 of their own and 3 community)
    players = {}
    for index, row in players_df.iterrows():
        players[row['Player']] = [row['Card1'], row['Card2']]
        players[row['Player']] = players[row['Player']] + first_three_community_cards
        players[row['Player']] = np.array(players[row['Player']])
        deck.remove(row['Card1'])
        deck.remove(row['Card2'])

    print(players)

    #create a matrix of all the permutations of 2 final cards out of remaining cards in deck
    remaining_cards_combinations = list(permutations(deck, 2))
    rcc_np = np.array(remaining_cards_combinations)


    #this function is to check and see edge case of other players having better score than you
    #It starts with the best hand combination for winning player and checks against other players
    #Stops when winning hand is acheived

    all_combinations_with_scores_descending = get_winning_player_combinations(players[winner], rcc_np)
    print(f"all_combinations_with_scores_descending: {all_combinations_with_scores_descending}")

    best_remaining_cards = []
    for combination in all_combinations_with_scores_descending:

        winning_player_score = int(combination[-1])

        best_remaining_cards = combination[5:7]
        winner_is_winning = True
        for player_name, player_hand in players.items():
            if player_name == winner:
                continue
            other_player_combination = np.append(player_hand, best_remaining_cards)
            other_player_score = score_my_hand(other_player_combination)
            if other_player_score >= winning_player_score:
                winner_is_winning = False
                break
        
        if winner_is_winning:
            return best_remaining_cards
    
    raise Exception('cannot find winning cards-split pot conditions')


first_three_community_cards = ['QC', 'AS', '7C']
winner = 'Lachlan'
best_remaining_cards = make_the_winner('players.csv', first_three_community_cards, winner)

print("best_remaining_cards: ", best_remaining_cards)
