from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
while True:
    mc.postToChat('Things that can be recycled: Paper, Plastic (bottles like gatorade,powerade,etc.), Aluminum(Soda cans) ,Steel cans, Newspaper,Corrugated Cardboard, Plastic bottles, Tin Cans')
    sleep(9.6)
