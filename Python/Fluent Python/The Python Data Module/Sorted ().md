```python 
import collections  
  
# 1. Setup the tools  
Card = collections.namedtuple('Card', ['rank', 'suit'])  
  
  
class FrenchDeck:  
        ranks = [str(n) for n in range(2, 11)] + list('JQKA')  
        suits = 'spades diamonds clubs hearts'.split()  
  
        def __init__(self):  
                self._cards = [Card(rank, suit) for suit in self.suits  
                               for rank in self.ranks]  
  
        def __len__(self):  
                return len(self._cards)  
  
        def __getitem__(self, position):  
                return self._cards[position]  
  
  
# 2. Create the Deck  
deck = FrenchDeck()  
  
# --- THIS IS THE PART FROM YOUR IMAGE ---  
  
# Define how much each suit is worth  
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  
  
  
def spades_high(card):  
	rank_value = deck.ranks.index(card.rank)
	return rank_value * len(suit_values) + suit_values[card.suit]
  
# Run the sort  
for card in sorted(deck, key=spades_high):  
        print(card)
# I know you don't know how to compare `Card` objects directly. So, before you compare two cards, pass them into the `spades_high` function. Take the **number** that comes out, and compare those numbers instead.

```