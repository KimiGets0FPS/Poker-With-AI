class Hand:
    def __init__(self, hole_cards, community_cards, hand=None):
        self.hole_cards = hole_cards
        self.community_cards = community_cards
        self.hand = hand

    def all_cards(self):
        return self.hole_cards + self.community_cards

    def get_hand(self):
        return self.hand


class HighCard(Hand):
    def __init__(self, hole_cards, community_cards, hand):
        super().__init__(hole_cards, community_cards, hand)

    def get_hand(self):
        return self.hand


class OnePair(Hand):
    def __init__(self, hole_cards, community_cards, hand="OnePair"):
        super().__init__(hole_cards, community_cards, hand)

    def get_hand(self):
        return self.hand


class TwoPair(OnePair):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "TwoPair")

    def get_hand(self):
        return self.hand


class ThreeOfAKind(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "ThreeOfAKind")

    def get_hand(self):
        return self.hand


class Straight(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "Straight")

    def get_hand(self):
        return self.hand


class Flush(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "Flush")

    def get_hand(self):
        return self.hand


class FullHouse(ThreeOfAKind, OnePair):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "FullHouse")

    def get_hand(self):
        return self.hand


class FourOfAKind(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "FourOfAKind")

    def get_hand(self):
        return self.hand


class StraightFlush(Hand, Flush, Straight):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "StraightFlush")

    def get_hand(self):
        return self.hand


class RoyalFlush(Hand, StraightFlush):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "RoyalFlush")

    def get_hand(self):
        return self.hand
