import random
import string

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
        return True





