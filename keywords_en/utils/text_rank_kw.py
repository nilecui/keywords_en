from __future__ import absolute_import, print_function, unicode_literals

# TextRank抽取关键词
from summa import keywords

class TextRankKeywords:
    def __init__(self):
        self.model = self.create_model()

    def create_model(self):
        pass

    def predict(self, text):
        kws = (keywords.keywords(text, words=5)).split("\n")
        return kws
