from random import shuffle


class Card:
    allowed_suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']

    def __init__(self, suit, value):
        if suit not in Card.allowed_suit:
            raise ValueError("Not a proper suit.")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.allowed_suit for value in (
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    ''' This line makes the deck iterable so you can thro card by card ''' 
    def __iter__(self):
    	return iter(self.cards)

    def count(self):
        t = 0
        for card in self.cards:
            t += 1
        return t

    def _deal(self, howMany):
        for i in range(howMany):
            if self.count() > 0:
                return self.cards.pop()
            else:
                raise ValueError("All cards have been dealt")

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full Decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, handsSize):
        hand = []
        for i in range(handsSize):
            hand.append(self.deal_card())
        return hand


myD = Deck()
myD.shuffle()
for card in myD:
	print(card)
