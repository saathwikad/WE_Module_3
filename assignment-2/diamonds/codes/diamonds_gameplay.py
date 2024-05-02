# gameplay.py

import random

# Sample deck of cards
deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Sample players and their initial scores
players = {
    "Player 1": 0,
    "Player 2": 0,
    "Player 3": 0,
    # Add more players if needed
}

def next_card_action():
    """Return a randomly chosen card from the deck."""
    return random.choice(deck)

def show_player_cards(player):
    """Return a list of cards for the given player."""
    # For simplicity, let's assume each player starts with a random hand of cards
    player_cards = random.sample(deck, k=5)
    return player_cards

def show_scores():
    """Return the current scores of all players."""
    return players
