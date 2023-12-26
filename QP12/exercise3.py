import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def card_value(card: Card) -> int:
    """Return the value of a card based on the game rules"""
    rank = card[1]
    if rank in "J Q K".split():
        value = 10
    elif rank == 'A':
        value = 11
    else:
        value = int(rank)

    if card[0] in "♠ ♣".split():  # black suits
        value *= 2
    return value

def play(seed_value: int) -> str:
    """Play a 4-player card game and return the winners"""
    random.seed(seed_value)

    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    # Play cards and calculate scores
    scores = {name: 0 for name in names}
    while any(hands[player] for player in hands):
        round_cards = {name: choose(hands[name]) for name in turn_order}
        round_values = {name: card_value(round_cards[name]) for name in turn_order}
        max_value = max(round_values.values())
        winners = [name for name, value in round_values.items() if value == max_value]

        for name in winners:
            scores[name] += 1

        for name in turn_order:
            hands[name].remove(round_cards[name])
            #print(f"{name}: {round_cards[name][0] + round_cards[name][1]:<3}  ", end="")
        #print()

    # Determine overall winners
    max_score = max(scores.values())
    overall_winners = [name for name, score in scores.items() if score == max_score]
    
    return " ".join(overall_winners)

if __name__ == "__main__":
    seed_value = 42  # Replace with your desired seed value
    winners = play(seed_value)
    #print(f"Overall Winners: {winners}")

