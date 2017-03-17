from twython import TwythonStreamer
from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import sleep

mc = Minecraft.create()
consumer_key = "huR85KlEvAAaeFuyZ2iz5o5gk"
consumer_secret = "5jCYjEqa1IzcgARH2lQ8o1zHdHQA3HjAxkjFnusBjtxUvMQrg1"
access_token = "775401076640088064-c5DfooidD0zHABH5d0nQX0jN8ZsGflc"
access_token_secret = "wbG4PRw72zBKBPnyS4fk7TI4Y2IwcJbPw8AeUQ897MkEa"
x, y, z = mc.player.getPos()
print (str(x) + ", " + str(y) + ", " + str(z))

def makeTree(t_xPos, t_yPos, t_zPos):

    mc.setBlock(t_xPos, (t_yPos + 3), (t_zPos + 3), tree)
    mc.postToChat("Thanks for recycling! A tree has been planted in your honor.")
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            x, y, z = mc.player.getPos()
            sleep(1)
            makeTree(x-5, y, z)
            print data['text'].encode('utf-8')

    def on_error(self, status_code, data):
        print status_code
stream = MyStreamer(consumer_key, consumer_secret,
access_token, access_token_secret)
term = "#LSHSRecycles"
stream.statuses.filter(track='twitter')
