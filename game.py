import random
from hand import *


def game(players):
    players_cards,  community_cards = get_cards(players)
    player_cards = players_cards[0]


def get_hand(player_cards: list[str], community_cards: list[str]) -> Hand:
    hand = Hand(player_cards, community_cards)

    count_suits = {}
    count_ranks = {}
    for i in range(len(hand.all_cards())):
        count_suits[hand.all_cards()[i][0]] = count_suits.get(hand.all_cards()[i][0], 0) + 1
        count_ranks[hand.all_cards()[i][1]] = count_ranks.get(hand.all_cards()[i][1], 0) + 1

    highest_hand = TwoPair(player_cards, community_cards)

    # Royal Flush

    # Straight Flush

    # Four of a Kind
    # Full House
    # Flush
    # Straight
    # Three of a Kind
    # Two pair
    # One Pair
    # High Card

    return highest_hand



def get_cards(players: int) -> tuple[list, list]:
    deck_of_cards = shuffle_cards(generate_cards())
    print(deck_of_cards)
    player_cards = [[] for _ in range(players)]
    community_cards = []

    for i in range(players * 2):
        player_cards[i % players].append(deck_of_cards[0])
        deck_of_cards.pop(0)

    for i in range(5):
        community_cards.append(deck_of_cards[0])
        deck_of_cards.pop(0)
        deck_of_cards.pop(0)  # Burn card

    return player_cards, community_cards

def generate_cards() -> list[str]:
    suits = ["♦", "♣", "♥", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck_of_cards = []
    for suit in suits:
        for rank in ranks:
            deck_of_cards.append(suit + rank)
    return deck_of_cards

def shuffle_cards(cards: list[str]) -> list[str]:
    random.shuffle(cards)
    return cards


if __name__ == '__main__':
    game(6)
