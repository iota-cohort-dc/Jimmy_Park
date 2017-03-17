class Deck(object):
    def __init__(self):
        self.deck = []

    def createDeck(self):
        suits = ["Heart","Diamond","Club","Spade"]
        values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
        for suit in suits:
            for val in values:
                card = Card(suit,val)
                self.deck.append(card)

        print self.deck
        return self.deck

    def shuffle(self):
        # random.shuffle(self.deck)
        # print self.deck
        # return self.deck
        pass

    def dealCards(self):
        # print "dealt card"
        # return (self.deck.pop(),self.deck.pop())
        # or
        print '--------------------------------------'

        val1 = self.deck.pop(0)
        val2 = self.deck.pop(1)
        cardpull = (val1,val2)
        print '--------------------------------------'
        print cardpull
        return cardpull

    def resetDeck(self):
        deck1.deck = []
        self. createDeck()
        print self.deck
        return self.deck

class Card(object):
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return "Card(Suit %r, Value %r)" % (self.suit, self.value)

deck1 = Deck() # creating object
print "Not shuffled"
deck1.createDeck() # creating the deck in the object
print "shuffled"
# deck1.shuffled() # shuffling the deck

print deck1.dealCards()


# deck1.createDeck()

# print deck1.dealCards()
# print deck1.dealCards()
# print deck1.dealCards()
# print deck1.dealCards()
