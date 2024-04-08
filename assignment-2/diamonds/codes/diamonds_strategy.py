import random

# Define the card values hierarchy
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5,
    '6': 6, '7': 7, '8': 8, '9': 9,
    'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
}

# Define player class
class Player:
    def _init_(self, name, is_human=False):
        self.name = name
        self.hand = []
        self.score = 0
        self.is_human = is_human

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def remove_card_from_hand(self, card):
        self.hand.remove(card)

    def choose_card_to_bid(self):
        if self.is_human:
            print(f"{self.name}'s hand: {self.hand}")
            while True:
                chosen_card = input(f"{self.name}, choose a card to bid (e.g., '2', '3', 'J'): ").strip().upper()
                if chosen_card in self.hand:
                    return chosen_card
                else:
                    print("Invalid card selection. Choose a card from your hand.")
        else:
            # Automated player (guest) bidding strategy: always bid with the highest available card
            chosen_card = max(self.hand, key=lambda card: card_values[card])
            self.remove_card_from_hand(chosen_card)
            return chosen_card

# Function to simulate an auction round
def auction_round(player1, player2, banker, diamond_card_value):
    print(f"\nDiamond card value: {diamond_card_value}")

    # Player 1 (human) bids
    player1_bid_card = player1.choose_card_to_bid()
    player1_bid_value = card_values[player1_bid_card]

    # Player 2 (automated) bids
    player2_bid_card = player2.choose_card_to_bid()
    player2_bid_value = card_values[player2_bid_card]

    # Banker (guest) bids
    banker_bid_card = banker.choose_card_to_bid()
    banker_bid_value = card_values[banker_bid_card]

    print(f"{player1.name} bids {player1_bid_card} ({player1_bid_value})")
    print(f"{player2.name} bids {player2_bid_card} ({player2_bid_value})")
    print(f"{banker.name} bids {banker_bid_card} ({banker_bid_value})")

    # Determine the winner of the auction
    max_bid_value = max(player1_bid_value, player2_bid_value, banker_bid_value)
    if player1_bid_value == max_bid_value:
        winner = player1
    elif player2_bid_value == max_bid_value:
        winner = player2
    else:
        winner = banker

    print(f"{winner.name} wins the auction!")
    winner.score += diamond_card_value

# Main function to simulate the game
def play_game():
    # Initialize players
    player_name = input("Enter your name: ")
    player1 = Player(player_name, is_human=True)
    player2 = Player("Automated Player")
    banker = Player("Banker (Guest)")

    # Generate a deck of diamond cards (values 2 to 14)
    diamond_cards = list(range(2, 15))

    # Shuffle the diamond cards
    random.shuffle(diamond_cards)

    # Deal diamond cards and start the game
    for diamond_card_value in diamond_cards:
        # Generate random cards for players and banker
        player1.add_card_to_hand(random.choice(list(card_values.keys())))
        player2.add_card_to_hand(random.choice(list(card_values.keys())))
        banker.add_card_to_hand(random.choice(list(card_values.keys())))

        # Simulate an auction round
        auction_round(player1, player2, banker, diamond_card_value)

    # Game over, display final scores
    print("\nGame over!")
    print(f"{player1.name}'s score: {player1.score}")
    print(f"{player2.name}'s score: {player2.score}")
    print(f"{banker.name}'s score: {banker.score}")

    # Determine the winner
    max_score = max(player1.score, player2.score, banker.score)
    if player1.score == max_score:
        print(f"{player1.name} wins!")
    elif player2.score == max_score:
        print(f"{player2.name} wins!")
    else:
        print(f"{banker.name} wins!")

# Start the game
play_game()