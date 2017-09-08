from modules.NLU import NLU
from modules.NLU.domains.student_info import get_user


class Bot:
    """
    the object will act as an interface between the NLU module and
    the websocket
    """

    # def __init__(self, username, password):
    def __init__(self):
        # self.user = get_user(username, password)
        self.user = get_user()
        self.nlu = NLU.NLU()

    def get_reply(self, query):
        reply = self.nlu.classify(query, self.user)
        return reply

bot = Bot()
bot.nlu.train()
bot.get_reply('my attendance in soft skills')

