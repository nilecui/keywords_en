"""Main module."""
from keywords_en.utils import TfIdfKeywords
from keywords_en.utils import TextRankKeywords 
from keywords_en.utils import TopicRankKeywords 
from keywords_en.utils import YakeKeywords 
from keywords_en.utils import KeyBertKeywords 

class KeyWordsEn:
    def __init__(self, algo_name="tfIdf", text=""):
        self.text = text
        self.algo_method = getattr(self, f'kw_{algo_name}', None)
        if not self.algo_method:
            raise NotImplementedError

        self.keywords = self.algo_method()

    def kw_tfIdf(self):
        kw_obj = TfIdfKeywords(use_stop_kw=False)
        kw_res = kw_obj.predict(self.text)
        return kw_res

    def kw_textRank(self):
        kw_obj = TextRankKeywords()
        kw_res = kw_obj.predict(self.text)
        return kw_res
         
    def kw_topicRank(self):
        kw_obj = TopicRankKeywords()
        kw_res = kw_obj.predict(self.text)
        return kw_res

    def kw_yake(self):
        kw_obj = YakeKeywords()
        kw_res = kw_obj.predict(self.text)
        return kw_res

    def kw_keyBert(self):
        kw_obj = KeyBertKeywords()
        kw_res = kw_obj.predict(self.text)
        return kw_res
