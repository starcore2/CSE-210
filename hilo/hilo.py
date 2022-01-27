import random


class Deck: #Deck Card
    deckOfCards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def drawRandom(card, deck): #The idea is that it will aways chose a random card and keep a full deck while ignoring the prevous card.
    new = deck.remove(card)
    choice = random.choice(new)
    return choice

class DrawnDeck: #This is for draw deck so I can return two values.
    def __init__(self, deck, card):
        self.deck = deck
        self.card = card

def drawDeck(deck): 
    #if len(deck) < 3: #The idea behind this was to have the deck return a empty deck but then i realised that it's not a good idea to check in the function.
    #    deck = Deck()
    #    return deck
    #else:
    card = random.choice(deck)
    deck = deck.remove(card)
    return DrawnDeck(deck, card)
    pass

def defaultCardCheck(choice, lastCard, newCard): 
    choice = choice.casefold()
    pointGain = 100  #What this allows is that I can modify the function to change the point gain or loss and even add two new variables so I can have main change theses values if needed.
    pointLoss = -75
    if choice == "h": #Check if picked higher
        if newCard > lastCard:
            return pointGain
        else: 
            return pointLoss
    elif choice == "l": #Check if the card is lower
        if newCard < lastCard:
            return pointGain
        else:
            return pointLoss
    else:
        print("Invalid choice")
        return False
    pass

def main():
    #Initalizing Game
    deck = Deck()
    print("What mode do you want? Do you wish to play 'Deck' or 'Random'")
    print("Deck mode basicly simulates drawing a card out of the deck. For example the first card will make the deck 12 cards.\nThe Next card drawn will make the deck 11 cards. Until a limit is reached then the deck gets reshuffled back to full.")
    print("Random just automaticly shuffles the deck back to full.")
    
    pass






if __name__ == "__main__":
    main()
