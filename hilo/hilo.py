import random
from tabnanny import check


class Deck: #Deck Card
    def __init__(self):
        self.deckOfCards = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def drawRandom(card, deck): #The idea is that it will aways chose a random card and keep a full deck while ignoring the prevous card.
    deck.remove(card)
    choice = random.choice(deck)
    return choice

class DrawnDeck: #This is for draw deck so I can return two values.
    def __init__(self, ddeck, dcard):
        self.ddeck = ddeck
        self.dcard = dcard

def drawDeck(deck): 
    #if len(deck) < 3: #The idea behind this was to have the deck return a empty deck but then i realised that it's not a good idea to check in the function.
    #    deck = Deck()
    #    return deck
    #else:
    card = random.choice(deck)
    deck.remove(card)
    return DrawnDeck(deck, card)
    

def defaultCardCheck(choice, lastCard, newCard): 
    choice = choice.casefold()
    pointGain = 100  #What this allows is that I can modify the function to change the point gain or loss and even add two new variables so I can have main change theses values if needed.
    pointLoss = -75
    if choice == "h" or choice == 'high': #Check if picked higher
        if newCard > lastCard:
            return pointGain
        else: 
            return pointLoss
    elif choice == "l" or choice == 'low': #Check if the card is lower
        if newCard < lastCard:
            return pointGain
        else:
            return pointLoss
    else:
        print("Invalid choice")
        return False
    

def main():
    #Initalizing Game
    deck = Deck()
    deck = deck.deckOfCards
    print("What mode do you want? Do you wish to play 'Deck' or 'Random'")
    print("Deck mode basicly simulates drawing a card out of the deck. For example the first card will make the deck 12 cards.\nThe Next card drawn will make the deck 11 cards. Until a limit is reached then the deck gets reshuffled back to full.")
    print("Random just automaticly shuffles the deck back to full.")
    x=0
    pointGain = 0
    score = 300
    deckDrawnFrom = drawDeck(deck)
    deck = deckDrawnFrom.ddeck
    lastCard = deckDrawnFrom.dcard
    newCard = -1
    HighLow = ""
    choice = ""
    while choice == "":
        choice = str(input("'Deck' or 'Random': "))
        choice = choice.casefold()
        if x>=1:
            print("Multiple invalid choice dected. Pick Deck or Random. If one of the options is not selected soon, the program will end.")
            if x>20:
                print("To many invalid choices attemtped.")
                choice = False
        if choice != 'deck' or choice != 'random' or choice == False:
            pass
        else:
            choice == ""
        x+=1
    while choice == 'deck':
        if len(deck) < 3:
            deck = Deck()
            deck = deck.deckOfCards
            deckDrawnFrom = drawDeck(deck)
            deck = deckDrawnFrom.ddeck
            lastCard = deckDrawnFrom.dcard
            print("Warning your deck has been suffled.")
            print(f"Your new first card is {lastCard}")
        else:
            print(f"Your Last Card was {lastCard}")
            print(f"Your deck has {len(deck)} cards left")
        print(f"Your current score is {score}")
        x=0
        HighLow=""
        while HighLow == "":
            HighLow = str(input("Pick High or Low [h/l]: "))
            HighLow = HighLow.casefold()
            if HighLow != 'h' or HighLow != 'l' or HighLow != 'high' or HighLow != 'low':
                pass
            else:
                HighLow = ""
        deckDrawnFrom = drawDeck(deck)
        newCard = deckDrawnFrom.dcard
        deck = deckDrawnFrom.ddeck

        try:
            pointGain = defaultCardCheck(HighLow, lastCard, newCard)
            score += pointGain
        except:
            print("Some how a invalide choice happend.") 
            choice = False
        print(f"The card was {newCard}")
        print(f"You have gain {pointGain} points")
        print(f"Your score is now {score}")
        lastCard=newCard
        print("Do you wish to keep playing?\n")
        x=0
        cont = ""
        while cont == "" and score > 0:
            cont = str(input("yes or no? [y/n]: "))
            if x>0:
                print("warning if you don't pick yes or no the program will assume no after more attempts")
                if x>20:
                    print("assuming no")
                    cont = 'n'
            x+=1
            if cont != "y" or cont != 'yes' or cont != 'n' or cont != 'no':
                pass
            else:
                cont = ""
        cont = cont.casefold()
        if cont == "n" or cont == "no":
            choice = False
        print("\n")
        if score < 0:
            print("You lost all of your points. Game Over")
            choice = False

    while choice == 'random':
        if len(deck) < 13:
            deck = Deck()
            deck = deck.deckOfCards
        print(f"Your Last Card was {lastCard}")
        print(f"Your current score is {score}")
        x=0
        HighLow=""
        while HighLow == "":
            HighLow = str(input("Pick High or Low [h/l]: "))
            HighLow = HighLow.casefold()
            if HighLow != 'h' or HighLow != 'l' or HighLow != 'high' or HighLow != 'low':
                pass
            else:
                HighLow = ""
        newCard = drawRandom(lastCard, deck)

        try:
            pointGain = defaultCardCheck(HighLow, lastCard, newCard)
            score += pointGain
        except:
            print("Some how a invalide choice happend.") 
            choice = False
        print(f"The card was {newCard}")
        print(f"You have gain {pointGain} points")
        print(f"Your score is now {score}")
        lastCard=newCard
        print("Do you wish to keep playing?\n")
        x=0
        cont = ""
        while cont == "" and score > 0:
            cont = str(input("yes or no? [y/n]: "))
            if x>0:
                print("warning if you don't pick yes or no the program will assume no after more attempts")
                if x>20:
                    print("assuming no")
                    cont = 'n'
            x+=1
            if cont != "y" or cont != 'yes' or cont != 'n' or cont != 'no':
                pass
            else:
                cont = ""
        cont = cont.casefold()
        if cont == "n" or cont == "no":
            choice = False
        print("\n")
        if score < 0:
            print("You lost all of your points. Game Over")
            choice = False
        pass

    print("Thank you for playing my game")
    if score > 0:
        print(f"Your final score was {score}")
    
    






if __name__ == "__main__":
    main()
