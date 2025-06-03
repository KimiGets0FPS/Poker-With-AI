class Hand:
    def __init__(self, hole_cards, community_cards, hand=None):
        self.hole_cards = hole_cards
        self.community_cards = community_cards
        self.hand = hand

    def all_cards(self):
        return self.hole_cards + self.community_cards

    def get_hand(self):
        return self.hand
    
    def get_highest_hand(self):
        cards = self.all_cards()
        list_suits = [card[0] for card in cards]
        list_ranks = [card[1:] for card in cards]

        


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
    def __init__(self, hole_cards, community_cards, hand="TwoPair"):
        super().__init__(hole_cards, community_cards, hand)


class ThreeOfAKind(Hand):
    def __init__(self, hole_cards, community_cards, hand="ThreeOfAKind"):
        super().__init__(hole_cards, community_cards, hand)

    def get_hand(self):
        return self.hand


class Straight(Hand):
    def __init__(self, hole_cards, community_cards, hand="Straight"):
        super().__init__(hole_cards, community_cards, hand)

    def get_hand(self):
        return self.hand


class Flush(Hand):
    def __init__(self, hole_cards, community_cards, hand="Flush"):
        super().__init__(hole_cards, community_cards, hand)

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


class StraightFlush(Flush, Straight):
    def __init__(self, hole_cards, community_cards, hand="StraightFlush"):
        super().__init__(hole_cards, community_cards, hand)

    def get_hand(self):
        return self.hand


class RoyalFlush(StraightFlush):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, "RoyalFlush")

    def get_hand(self):
        return self.hand
