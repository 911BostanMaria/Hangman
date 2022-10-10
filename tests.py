import unittest
from domain import Hangman
from repository import Game


class Tests(unittest.TestCase):
    def setUp(self):
        self._game = Game(hangman=Hangman("anna has apples", 0))

    def test_create_hangman_word(self):
        word = self._game.create_hangman_word()
        self.assertEqual(word, 'a__a has a____s')

    def test_find_letter(self):
        word = self._game.create_hangman_word()
        self.assertEqual(self._game.find_letter(word, 'n'), 'anna has a____s')

    def test_game_won(self):
        self.assertEqual(self._game.game_won("anna has apples"), 1)
