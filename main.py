from repository import Game
from domain import Hangman
import random


class UserInterface:
    def __init__(self):
        self._data = []

    def add_sentences_in_data(self):
        with open('input.txt') as f:
            content = f.read()
            tokens = content.split('\n')
            for token in tokens:
                self._data.append(token)

    def add_sentences_in_file(self):
        count = 0
        while count <= 4:
            ok = True
            sentences = [] * 5
            while ok is True:
                ok = False
                user_input = input("Add sentences >>>")
                user_input = user_input.lower()
                words = user_input.split(" ")
                if len(words) < 3:
                    print("Not enough words in sentence.")
                elif user_input in sentences:
                    print("Duplicate sentence.")
                else:
                    sentences.append(user_input)
                    ok = True
                    count = count + 1
                    if count == 5:
                        ok = False
        return sentences

    def pick_random_sentence(self):
        number = random.randint(0, len(self._data)-1)
        return self._data[number]

    def write_in_txt_file(self, sentences):
        with open('input.txt', 'w') as f:
            for line in sentences:
                f.write(line)
                f.write('\n')

    def main(self):
        sentences = self.add_sentences_in_file()
        self.write_in_txt_file(sentences)
        self.add_sentences_in_data()
        sentence = self.pick_random_sentence()
        hangman = Hangman(sentence, 0)
        game = Game(hangman)
        hidden_sentence = game.create_hangman_word()
        print("The game has started. \n")
        while hangman.score < 7:
            print(hidden_sentence + hangman.display_score())
            if game.game_won(hidden_sentence):
                print(sentence)
                print("You won! :)")
                return
            ok = True
            while ok:
                ok = False
                user_input = input("Guess a letter >>> ")
                user_input.lower()
                if not ord('a') <= ord(user_input) <= ord('z'):
                    print('Invalid input. Try again')
                    ok = True
            game.play_game(hidden_sentence, user_input)
            hidden_sentence = game.find_letter(hidden_sentence, user_input)
        if hangman.score == 7:
            print("You lost. :(")
            return


k = UserInterface()
k.main()