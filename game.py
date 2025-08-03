import random

from hand import *


def game(players: int):
    players_cards,  community_cards = get_cards(players)
    player_cards = players_cards[0]


def get_hand(player_cards: list[str], community_cards: list[str]) -> Hand:
    hand = Hand(player_cards, community_cards)

    count_suits = {}
    count_ranks = {}
    for i in range(len(hand.all_cards())):
        count_suits[hand.all_cards()[i][0]] = count_suits.get(hand.all_cards()[i][0], 0) + 1
        count_ranks[hand.all_cards()[i][1]] = count_ranks.get(hand.all_cards()[i][1], 0) + 1

    # Checking for flush

    flush = False
    for suit in count_suits:
        if count_suits[suit] == 5:
            flush = True

    # Checking for straight and pairs

    straight, straight_count, highest_card = False, 0, ""
    pair = 0
    three_of_a_kind = False
    four_of_a_kind = False
    for rank in count_ranks:
        if count_ranks[rank] == 2:
            pair += 1
        if count_ranks[rank] == 3:
            three_of_a_kind = True
        if count_ranks[rank] == 4:
            four_of_a_kind = True

    # Start Determining hand
    if flush and straight and highest_card == "A":
        return Hand(player_cards, community_cards, 10, 15)
    elif flush and straight:  # Straight Flush
        return Hand(player_cards, community_cards, 9, get_card_value(highest_card, True))
    elif four_of_a_kind:  # Four of a Kind
        return Hand(player_cards, community_cards, 8, get_card_value(highest_card, False))
    elif three_of_a_kind and pair >= 1:  # Full House
        return Hand(player_cards, community_cards, 7, get_card_value(highest_card, True))
    elif flush:  # Flush
        return Hand(player_cards, community_cards, 6, get_card_value(highest_card, False))
    elif straight:  # Straight
        return Hand(player_cards, community_cards, 5, get_card_value(highest_card, True))
    elif three_of_a_kind:  # Three of a Kind
        return Hand(player_cards, community_cards, 4, get_card_value(highest_card, True))
    elif pair >= 1:  # Two Pair
        return Hand(player_cards, community_cards, 3, get_card_value(highest_card, True))
    elif pair == 1:  # Pair
        return Hand(player_cards, community_cards, 2, get_card_value(highest_card, True))
    # High Card
    return Hand(player_cards, community_cards, 1, get_card_value(highest_card, True))


def get_card_value(card_rank, straight=False) -> int:
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    if straight and card_rank == "A":
        return 1
    for i in range(len(ranks)):
        if card_rank == ranks[i]:
            return i+2
    return 0


def get_cards(players: int) -> tuple[list, list]:
    deck_of_cards = shuffle_cards(generate_cards())
    print(deck_of_cards)
    player_cards = [[] for _ in range(players)]
    community_cards = []

    for i in range(players * 2):
        player_cards[i % players].append(deck_of_cards[0])

    for i in range(7):
        if i != 0 or i != 4 or i != 6:
            community_cards.append(deck_of_cards[i])

    return player_cards, community_cards


def generate_cards() -> list[Card]:
    suits = ["♦", "♣", "♥", "♠"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck_of_cards = []
    for suit in suits:
        for rank in ranks:
            deck_of_cards.append(Card(suit, rank))
    return deck_of_cards


def shuffle_cards(cards: list[Card]) -> list[Card]:
    random.shuffle(cards)
    return cards


if __name__ == '__main__':
    game(6)
