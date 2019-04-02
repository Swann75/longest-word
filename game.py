import random
import string
import requests

class Game():
    def __init__(self):
        self.grid = [random.choice(string.ascii_uppercase) for x in range(9)]

    def isvalid(self, word):
        if len(word) == 0:
            return False
        for letter in word:
            if letter not in self.grid:
                return False
            self.grid.remove(letter)

        r = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
        json = r.json()
        if json['found'] == False:
            return False
        return True






