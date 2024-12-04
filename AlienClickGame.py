import pgzrun
from random import randint

TITLE = "You hit it!"

WIDTH = 500
HEIGHT = 500

alien = Actor("aliensprite")

Message = ""

def draw():
    screen.clear()
    screen.fill(color =(120,0,0))
    alien.draw()
    screen.draw.text(Message,center=(400,10),fontsize = 30)

pgzrun.go()