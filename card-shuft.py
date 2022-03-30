import random
from tkinter import *
faces= ["Ace", "Deuce", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King" ]
    
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


""" class Card:
    Class that represents one palying card
    #class attributes faces and suits contains string that correspond to card face and suit values
    faces= ["Ace", "Deuce", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten",
            "Jack", "Queen", "King" ]
    
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self,face,suit):
        self.face = face
        self.suit = suit

        def __str__(self):
            String representation of a card
            return "%s of %s" %(self.face, self.suit)
 """
class Deck(Frame):
    """Class to represent a GUI card deck shuffler"""

    def __init__(self):
        """Deck constructor"""
        Frame.__init__(self)
        self.master.title("Card Dealing Program")
        self.deck = [] #List of card objects
        self.currentCard = 0 #index of current card 

        #create deck

        for i in range(52):
            self.deck.append(faces[int(i%13)] + " " + suits[int(i/13)]) 

            """ self.deck.append(Card(Card.faces[int(i%13)], Card.suits[int(i/13)])) """
            
        

        #Create Buttons
        self.dealButton = Button(self, text="Deal Card", width=10, command=self.dealCard)
        self.dealButton.grid(row=0, column=0)

        self.shuffleButton = Button(self, text="Shuffle Cards", width=10, command=self.shuffle)
        self.shuffleButton.grid(row=0, column=1)

        #Create Labels
        self.message1 = Label(self, height=2, text="Welcome to Card Dealer!")
        self.message1.grid(row=1, columnspan=2)

        self.message2 = Label(self, height=2, text="Deal card or shuffle deck")
        self.message2.grid(row=2, columnspan=2)

        self.shuffle()
        self.grid()

    def shuffle(self):
        """Shuffle the deck"""

        self.currentCard = 0

        for i in range(len(self.deck)):
            j =  random.randint(0,51)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

            self.message1.config(text="DECK IS SHUFFLED")
            self.message2.config(text="")
            self.dealButton.config(state=NORMAL)

    def dealCard(self):
        """Deal one card from the deck"""

        #display the card if it exist
        if self.currentCard < len(self.deck):
            self.message1.config(text=self.deck[self.currentCard])
            self.message2.config(text="Card #: %d" % self.currentCard)
        else:
            self.dealButton.config(state=DISABLED)
            self.message1.config(text="NO MORE CARDS TO DEAL")
            self.message2.config(text ="Shuffle cards to continue")
            self.dealButton.config(state=DISABLED)

        self.currentCard += 1 #increment card for next turn

    def main():
        Deck().mainloop()


Deck().mainloop()