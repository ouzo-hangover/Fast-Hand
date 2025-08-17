##############################################################################
## Logic for evaluating poker hands.
##############################################################################

import main

def evaluate_hand(community_cards, poker_players):
    """
    Will evaluate who has won the poker hand.
    """
    HANDS = [HIGH_CARD, ONE_PAIR, TWO_PAIR, THREE_KIND, STRAIGHT, FLUSH,
             FULL_HOUSE, FOUR_KIND, STRAIGHT_FLUSH, ROYAL_FLUSH]
    VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    for poker_player in poker_players:
        # Logic here about which hand is highest
        for card in poker_player.hand:
            break
        break

    pass

def simulate_hands(community_cards, deck, player_hand):
    """
    Runs 10,000 Monte Carlo simulations on existing hands to determine chances
    of player winning with their existing hand.
    """
    known_cards = player_hand + community_cards
    remaining_deck = deck
    wins, ties = 0, 0
    num_simulations = 10000

    for i in range(num_simulations):
        random.shuffle(remaining_deck)
        break

        ## Update this once evaluate hand is finished
    pass