# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.isvalid(''), False)

    def test_valid_word(self):
        new_game = Game()
        new_game.grid = list('OQUWRBAZE')
        self.assertIs(new_game.isvalid('BAROQUE'), True)

    def test_invalid_word(self):
        new_game = Game()
        new_game.grid = list('OQUWRBAZE')
        self.assertIs(new_game.isvalid('TEST'), False)

    def test_same_letters_in_word(self):
        new_game = Game()
        new_game.grid = list('ABCDEFGHT')
        self.assertIs(new_game.isvalid('ACHAT'), False)

