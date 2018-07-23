import collections
from random import choice  # <1>

Card = collections.namedtuple('Card', ['rank', 'suit'])  # <2>


class FrenchDeck:  # <3>
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # <4>
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):  # <5>
        self._cards = [Card(rank, suit) for suit in self.suits  # <6>
                       for rank in self.ranks]

    def __len__(self):  # <7>
        return len(self._cards)

    def __getitem__(self, position):  # <8>
        return self._cards[position]


deck = FrenchDeck()
print("deck.ranks", deck.ranks)
print("deck.suits", deck.suits)

print("len(deck)", (len(deck)))

print("deck[1]", deck[1])

print("choice(deck)", choice(deck))

print("deck[12]", deck[12])
print("deck[12::13]", deck[12::13])

# just by implementing the __getitem__ special method,
# our deck is also iterable
for card in deck:
    print(card)
