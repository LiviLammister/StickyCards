from flashcard import Flashcard
import glob, json, pathlib

class Deck:
    
    def __init__(self, name = None):
        """ Creates a deck
        If a name is provided, the deck already exists and will load cards
        from JSONs located therein.  If no name is provided, the user
        will be prompted to create a new deck.  The name of the deck is the
        name of the directory that contains its cards.
        
        @NOTE In the case where a new deck is being created from scratch, the
              program does not detect if a deck with that name already exists.
        """
        self.flashcards = []
        self.name = ''
        if name is None:
            """ Create new deck directory"""
            newDeckName = input('Enter name of deck: ')
            pathlib.Path('./Decks/' + newDeckName).mkdir(parents=True,
                         exist_ok=True)
            self.name = newDeckName
        else:
            self.name = name
            self.load_cards()
    
    def add_new_card(self):
        
    def load_cards(self):
        """ Import existing card data
        Imports card data from JSONs located in cardDirectory into card list.
        DIRECTORY IS LOCATED IN OBJECT NOW
        """
        flashcardJSONs = glob.glob(self.name + '/*.json') 
        for item in flashcardJSONs:
            print(item)
            with open(item, 'r') as f:
                self.flashcards.append(json.load(f))
    
    def save_cards(self):
        """ Export card data
        Exports card data into JSONs located in a given directory.
        """
        for item in self.flashcards:
            with open(item.get("filename"), 'w') as f:
                json.dump(item, f)
    
    def list_cards(self):
        """ Lists all cards in deck"""
        for item in self.flashcards:
            print(item)

""" Testing Area """