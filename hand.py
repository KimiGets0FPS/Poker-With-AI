class Hand:
    def __init__(self, hole_cards, community_cards, hand=None, value=None):
        self.hole_cards = hole_cards
        self.community_cards = community_cards
        self.hand = hand
        self.value = value

        self.suits = ["♦", "♣", "♥", "♠"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def all_cards(self):
        return self.hole_cards + self.community_cards

    def get_hand(self):
        return self.hand

    def get_value(self):
        return self.value

    def get_rank_from_value(self):
        return self.ranks[self.get_value()-2]

    def get_higher_hand(self, other_hand: super()) -> 1 or 0 or -1:
        # 1 means this player wins
        # 0 means tie
        # -1 means this player loses
        if self.hand > other_hand.get_hand():
            return 1
        return 0


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

        self._suits = ["♦", "♣", "♥", "♠"]
        self._ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

# class HighCard(Hand):
#     def __init__(self, hole_cards, community_cards, hand):
#         super().__init__(hole_cards, community_cards, hand)
#
#     def get_hand(self):
#         return self.hand
#
#
# class OnePair(Hand):
#     def __init__(self, hole_cards, community_cards, hand="OnePair"):
#         super().__init__(hole_cards, community_cards, hand)
#
#     def get_hand(self):
#         return self.hand
#
#
# class TwoPair(OnePair):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "TwoPair")
#
#     def get_hand(self):
#         return self.hand
#
#
# class ThreeOfAKind(Hand):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "ThreeOfAKind")
#
#     def get_hand(self):
#         return self.hand
#
#
# class Straight(Hand):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "Straight")
#
#     def get_hand(self):
#         return self.hand
#
#
# class Flush(Hand):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "Flush")
#
#     def get_hand(self):
#         return self.hand
#
#
# class FullHouse(ThreeOfAKind, OnePair):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "FullHouse")
#
#     def get_hand(self):
#         return self.hand
#
#
# class FourOfAKind(Hand):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "FourOfAKind")
#
#     def get_hand(self):
#         return self.hand
#
#
# class StraightFlush(Hand, Flush, Straight):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "StraightFlush")
#
#     def get_hand(self):
#         return self.hand
#
#
# class RoyalFlush(Hand, StraightFlush):
#     def __init__(self, hole_cards, community_cards):
#         super().__init__(hole_cards, community_cards, "RoyalFlush")
#
#     def get_hand(self):
#         return self.hand
