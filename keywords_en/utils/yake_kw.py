from __future__ import absolute_import, print_function, unicode_literals

# YACK关键词抽取
# YACK一种基于文档中提取的功能，是一种无监督的关键字提取算法，它是多种语言：英语，意大利语，德语，荷兰语，西班牙语，芬兰语，法语，波兰语，土耳其语，葡萄牙语和阿拉伯语。
from yake import KeywordExtractor


class YakeKeywords:
    def __init__(self):
        self.model = self.create_model()

    def create_model(self):
        model = KeywordExtractor(lan="en", n=1, top=5)
        return model

    def predict(self, text):
        keywords = self.model.extract_keywords(text=text)
        l_keywords = [x for x, y in keywords]
        return l_keywords

if __name__=="__main__":
    obj = YakeKeywords()
    res = obj.predict('The Free Software Foundation (FSF) is a nonprofit with a worldwide mission to promote computer user freedom. Escape to Freedom now also available in Mandarin and Spanish "Escape to Freedom" is a new animated video from the Free Software Foundation (FSF), giving an introduction to the concepts behind software freedom: both what we gain by having it, and what rights are at stake. We now have the video available in Mandarin and Spanish language tracks. 2022 Bulletin: "Unjust Algorithms" by Zoë Kooyman Developments in artificial intelligence (AI) injustices have rapidly taken a turn for the worse in recent years. Algorithmic decision-making systems are used more than ever by organizations, educational institutions, and governments looking for ways to increase understanding and make predictions. The Free Software Foundation (FSF) is working through this issue, and its many scenarios, to be able to say useful things about how this relates to software freedom. Our call for papers on Copilot was a first step in this direction. Free software means that the users have the freedom to run, edit, contribute to, and share the software. Thus, free software is a matter of liberty, not price. We have been defending the rights of all software users for the past 35 years. Help sustain us for many more; become an associate member today. Subscribe to our monthly newsletter, the Free Software Supporter: Our initiatives Defective by Design is a grassroots campaign to eliminate Digital Restrictions Management (DRM) in media and devices. Read the Email Self-Defense Guide to get started with email encryption, a skill necessary to combat bulk surveillance. The End Software Patents initiative fights to abolish software patents around the world. Join us in calling for a Web that respects our freedom by being compatible with free software and stand up against nonfree JavaScript. The Free Software Directory is a collaborative catalog of computer programs and apps that are fully free. The GNU operating system is a continuously evolving, complete operating system made entirely of free software. LibrePlanet is our global network of free software activism, including events like our annual conference, and online collaboration spaces. The Licensing and Compliance Lab is the preeminent resource for public education on licensing best practices and enforcing the GPL. The "Respects Your Freedom" program certifies retailers who sell hardware in a manner that respects the rights of their users. "This community that we have, that were building, that does so much, has to grow. We cant compete with Apple, we cant compete with Google, directly, in the field of resources. What we can eventually do is head count and heart count. We can compete on the ground of ideology because ours is better." -- Edward Snowden, NSA whisteblower, speaking at LibrePlanet 2016. Take Action Bulletin Old but not forgotten Unjust Algorithms Verifying free software: The basics The need for free software education now Overcoming the hurdle of "industry standard" in education technology Read the current issue of the Bulletin and check out the archives. Shop Beat the summer heat with a stylish GNU baseball cap!')
    print(res)
