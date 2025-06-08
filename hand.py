class Hand:
    def __init__(self, hole_cards, community_cards, hand=None, value=0):
        self.hole_cards = hole_cards
        self.community_cards = community_cards
        self.hand = hand
        self.value = value

    def get_all_cards(self):
        return self.hole_cards + self.community_cards

    def get_hand(self):
        return self.hand
    
    def get_value(self):
        return self.value
    
    def compare_hands(self, other_hand):
        ...


class HighCard(Hand):
    def __init__(self, hole_cards, community_cards, hand):
        super().__init__(hole_cards, community_cards, hand, value=1)

    def get_hand(self):
        return self.hand


class OnePair(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="OnePair", value=2)

    def get_hand(self):
        return self.hand


class TwoPair(Hand, OnePair):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="TwoPair", value=3)


class ThreeOfAKind(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="ThreeOfAKind", value=4)

    def get_hand(self):
        return self.hand


class Straight(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="Straight", value=5)

    def get_hand(self):
        return self.hand


class Flush(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="Flush", value=6)

    def get_hand(self):
        return self.hand


class FullHouse(ThreeOfAKind, OnePair):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="FullHouse", value=7)

    def get_hand(self):
        return self.hand


class FourOfAKind(Hand):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="FourOfAKind", value=8)

    def get_hand(self):
        return self.hand


class StraightFlush(Hand, Flush, Straight):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="StraightFlush", value=9)

    def get_hand(self):
        return self.hand


class RoyalFlush(Hand, StraightFlush):
    def __init__(self, hole_cards, community_cards):
        super().__init__(hole_cards, community_cards, hand="RoyalFlush", value=10)

    def get_hand(self):
        return self.hand
