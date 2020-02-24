import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),os.pardir,"src"))
import sida.slackbot.bot as bot

def test_send():
    assert bot.send("test_slackbot", 0)==-1
    assert bot.send("test_slackbot", 1, bot.channel_sida)==0