import random
import unittest
from domain import Hangman
import texttable

class Game:
    def __init__(self, hangman):
        self._hangman = hangman

    def create_hangman_word(self):
        """
        :return: Creates hangman-style sentence and returns it.
        anna has apples -> a__a h_s a____s
        """
        token = self._hangman.sentence.split(" ")
        length = len(token) - 1
        letters = []*(len(token)*2+1)
        new_word = ""
        i = 0
        while i <= length:
            letters.append(token[i][0])
            letters.append(token[i][len(token[i])-1])
            i = i+1
        i = 0
        while i <= length:
            for j in range(0, len(token[i])):
                found = 0
                if j == 0 or j == len(token[i])-1:
                    new_word = new_word + token[i][j]
                else:
                    for k in letters:
                        if token[i][j] == k:
                            found = 1
                    if j !=0 and j != len(token[i])-1:
                        if found:
                            new_word = new_word + token[i][j]
                        else:
                            new_word = new_word + '_'
            new_word = new_word + " "
            i = i+1
        return new_word

    def find_letter(self, hangman_sentence, user_guess):
        """
        :param user_guess: A letter the user picked. If the letter is found in the hangman-word, then each occurrence
        of the letter is revealed, else score increases
        else the score increases
        :param hangman_sentence: The hangman-style new sentence. (a__a h_s a____s)
        """
        new_word = ""
        found = 0
        pos = 0
        position = [0]*(len(self._hangman.sentence)+1)
        word = self._hangman.sentence.split(" ")
        how_many_words = len(word)
        count = 0
        while count < how_many_words:
            for i in range(0, len(word[count]) - 1):
                if user_guess == word[count][i]:
                    found = 1
                    position[pos] = user_guess
                pos = pos + 1
            count = count + 1
            pos = pos + 2 # to include space between words
        if found == 1:
            for i in range(0,len(hangman_sentence)):
                if position[i] != 0:
                    new_word = new_word + user_guess
                else:
                    new_word = new_word + hangman_sentence[i]
            hangman_sentence = ""
            for i in new_word:
                hangman_sentence = hangman_sentence + i
        return hangman_sentence

    def play_game(self, hangman_sentence, user_guess):
        """
        :param hangman_sentence: The sentence hangman-styled (a__a has a____s)
        :param user_guess: User input, a single letter.
        :return: None. Checks if user input is found in the sentence using the find_letter function,
        if not found, increases score.
        """
        initial = hangman_sentence
        hangman_sentence = self.find_letter(hangman_sentence, user_guess)
        if hangman_sentence == initial:
            self._hangman.score = self._hangman.score + 1

    def game_won(self, hangman_sentence):
        if self._hangman.score != 7:
            for i in hangman_sentence:
                if i == "_":
                    return 0
        return 1
