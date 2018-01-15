class Flashcard:
    """ Flashcard
    (Will add more information later)
    """
    
    def __init__(self, deck, JSONFilename = None):
        """ Create new card
        Creates a new card from existing JSON data or from scratch.  If no
        JSON is provided, the user is prompted to input required data.
        """
        self.data = {}
        self.deck = deck
        self.name = ''
        
        if JSONFilename is None:
            self.data['question'] = input('What is the question on this card? ')
            self.data['answer'] = input('What is the answer on this card? ')
            self.data['timesAsked'] = 0
            self.data['correctlyAnswered'] = 0
            """ 
            Set last time reviewd to time card is created since it has not
            been reviewed yet.
            """
            self.data['lastTimeReviewed'] = str(datetime.datetime.now())
            self.name = input('Lastly, what is the name of this card? ')   
        else:
            with open(JSONFilename, 'r') as f:
                self.data = json.load(f)  
            self.name = JSONFilename
    
    # def export(self):
        """ Exports card data to a JSON """
    
    def show_data(self):
        """ Show data contained in Flashcard """
        print(self.name)
        print(self.data)

""" Testing Area """
testCard = Flashcard()
testCard.show_data()