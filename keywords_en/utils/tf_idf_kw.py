from __future__ import absolute_import, print_function, unicode_literals

from itertools import islice
from tqdm.notebook import tqdm
from re import sub
import torch
from .stop_keywords import StopKeywords

from sklearn.feature_extraction.text import CountVectorizer
from numpy import array, log

class TfIdfKeywords:
    def __init__(self, use_stop_kw=False):
        self.model = self.create_model()
        self.use_stop_kw = use_stop_kw
        if self.use_stop_kw:
            self.kws = self.create_keywords()

    def create_model(self):
        vectorizer = CountVectorizer()
        return vectorizer

    def create_keywords(self):
        stop_obj = StopKeywords("stop_keywords.csv")
        stop_kws = stop_obj.get_keywords()

        return stop_kws

    def predict(self, text):
        tf = self.model.fit_transform([text.lower()])
        tf = tf.toarray()
        tf = log(tf + 1)
        tfidf = tf.copy()
        words = array(self.model.get_feature_names())
        if self.use_stop_kw:
            for k in tqdm(self.kws.keys()):
                if k in words:
                    tfidf[:, words == k] = tfidf[:, words == k] * self.kws[k]

        for j in range(tfidf.shape[0]):
            keywords = words[tfidf[j, :].argsort()[-5:][::-1]]
        return keywords

if __name__=="__main__":
    obj = TfIdfKeywords(use_stop_kw=True)
    res = obj.predict('The Free Software Foundation (FSF) is a nonprofit with a worldwide mission to promote computer user freedom. Escape to Freedom now also available in Mandarin and Spanish "Escape to Freedom" is a new animated video from the Free Software Foundation (FSF), giving an introduction to the concepts behind software freedom: both what we gain by having it, and what rights are at stake. We now have the video available in Mandarin and Spanish language tracks. 2022 Bulletin: "Unjust Algorithms" by Zoë Kooyman Developments in artificial intelligence (AI) injustices have rapidly taken a turn for the worse in recent years. Algorithmic decision-making systems are used more than ever by organizations, educational institutions, and governments looking for ways to increase understanding and make predictions. The Free Software Foundation (FSF) is working through this issue, and its many scenarios, to be able to say useful things about how this relates to software freedom. Our call for papers on Copilot was a first step in this direction. Free software means that the users have the freedom to run, edit, contribute to, and share the software. Thus, free software is a matter of liberty, not price. We have been defending the rights of all software users for the past 35 years. Help sustain us for many more; become an associate member today. Subscribe to our monthly newsletter, the Free Software Supporter: Our initiatives Defective by Design is a grassroots campaign to eliminate Digital Restrictions Management (DRM) in media and devices. Read the Email Self-Defense Guide to get started with email encryption, a skill necessary to combat bulk surveillance. The End Software Patents initiative fights to abolish software patents around the world. Join us in calling for a Web that respects our freedom by being compatible with free software and stand up against nonfree JavaScript. The Free Software Directory is a collaborative catalog of computer programs and apps that are fully free. The GNU operating system is a continuously evolving, complete operating system made entirely of free software. LibrePlanet is our global network of free software activism, including events like our annual conference, and online collaboration spaces. The Licensing and Compliance Lab is the preeminent resource for public education on licensing best practices and enforcing the GPL. The "Respects Your Freedom" program certifies retailers who sell hardware in a manner that respects the rights of their users. "This community that we have, that were building, that does so much, has to grow. We cant compete with Apple, we cant compete with Google, directly, in the field of resources. What we can eventually do is head count and heart count. We can compete on the ground of ideology because ours is better." -- Edward Snowden, NSA whisteblower, speaking at LibrePlanet 2016. Take Action Bulletin Old but not forgotten Unjust Algorithms Verifying free software: The basics The need for free software education now Overcoming the hurdle of "industry standard" in education technology Read the current issue of the Bulletin and check out the archives. Shop Beat the summer heat with a stylish GNU baseball cap!')
    print(res)
