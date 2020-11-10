import os
import requests
import re

class Poem:

    def __init__(self, content):
        '''constructor for a poem object'''

        self.content = content
        self.evaluation = 0


    def tighten_up(self):
        '''This function 'tightens up' the poem stylistically'''

        changes = 0
        
        hate_to_love = self.hate_to_love()
        self.content = hate_to_love[0]
        changes+=hate_to_love[1]

        insert_alliteration = self.insert_alliteration()
        self.content = insert_alliteration[0]
        changes+=insert_alliteration[1]

        self.evaluation = changes

        return changes



    def insert_alliteration(self):
        '''This function adds alliteration, which is pleasing to humans'''

        changes = 0 #calculates the number of changes made to the poem
        lines = self.content
        for i in range(len(lines)):
            tokens = lines[i].split(' ')
            letter = tokens[0][0].lower()
            for token in tokens:
                try:
                    thesaurus = requests.get("https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=77adfd9b-5f1a-4b00-ad21-94076a899e1b".format(token))
                    syns = thesaurus.json()[0]["meta"]["syns"]
                    for syn in syns:
                        if syn[0] == (letter):
                            syn = syn[0].upper()
                            tokens[i] = syn
                            changes+=1
                except:
                    pass
            lines[i] = ' '.join(tokens)

        return (lines, changes)


    def hate_to_love(self):
        '''Turns mean words and phrases into loving alternatives'''

        changes = 0 #calculates the number of changes made to the poem
        lines = self.content
        hate_words = ["crazy", "stupid", "dumb", "corrupt", "idiot", "shame", "Dumb", "dumb", "moron", "Hunter", "shut"]
        for i in range(len(lines)):
            tokens = lines[i].split(' ')
            for token in tokens:
                if token in hate_words:
                    thesaurus = requests.get("https://www.dictionaryapi.com/api/v3/references/thesaurus/json/{}?key=77adfd9b-5f1a-4b00-ad21-94076a899e1b".format(tokens[i]))
                    ants = thesaurus.json()[0]["meta"]["ants"]
                    tokens[i] = ants[i]
                    changes+=1
            lines[i] = ' '.join(tokens)
        
        return (lines, changes)
    
    def speak(self):
        '''Recites the poem from the operating system'''

        for line in self.content:
            print(line) #print

        for line in self.content:
            os.system("say " + re.sub(r'[^\w\s]','',line)) #speak





