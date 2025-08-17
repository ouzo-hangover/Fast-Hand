##############################################################################
## Main game logic.
##############################################################################

import random
import itertools

community_cards = []
deck = []
SUITS = ('♠ Spade', '♥ Heart', '♦ Diamond', '♣ Club')
RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

class PokerPlayer:
    num_players = 0

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wins = 0
        PokerPlayer.num_players += 1

    def add_card(self, card):
        self.hand.append(card)

def create_deck():
    """
    Creates a standard 52 card deck.
    """

    return list(itertools.product(RANKS, SUITS))

def pull_card(deck):
    """
    This will pull one card from the top of the deck.
    """
    pulled_card = deck.pop()
    return pulled_card

def flop(deck, poker_players):
    """
    Hands out the initial 2 cards per player, burn 1 card, and then places 3
    cards onto the table.
    """
    global community_cards

    # Deals cards to players and bots.
    for i in range(0, len(poker_players)):
        for j in range(2):
            card = pull_card(deck)
            poker_players[i].add_card(card)

    # Burn one card.
    deck.pop()

    # Deal the community cards/ flop.
    for i in range(3):
        community_cards.append(pull_card(deck))

    return

def turn():
    """
    Adds one card to the community cards, if player raises.
    """
    pass

def river():
    """
    Adds one cards to the community cards, if player raises after the turn.
    """
    pass




def main():

    global community_cards
    global deck

    # Empty list of players to start
    poker_players = []

    #player_name = input("What's your player name: ")
    player = PokerPlayer('ouzo')
    poker_players.append(player)

    # Add in a bot to play against
    bot1 = PokerPlayer('bot1')
    poker_players.append(bot1)

    while True:

        # Create a fresh deck and shuffle every round
        deck = create_deck()
        random.shuffle(deck)
        flop(deck, poker_players)

        break

    return

if __name__ == '__main__':
    main()