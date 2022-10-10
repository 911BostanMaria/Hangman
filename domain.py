class Hangman:
    def __init__(self, sentence, score):
        self._sentence = sentence
        self._score = score

    @property
    def score(self):
        return self._score

    def display_score(self):
        d = {0: '',
           1: 'h',
           2: 'ha',
           3: 'han',
           4: 'hang',
           5: 'hangm',
           6: 'hangma',
           7: 'hangman'}
        return d[self._score]

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def sentence(self):
        return self._sentence
