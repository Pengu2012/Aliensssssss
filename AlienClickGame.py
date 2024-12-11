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
def place_alien():
    alien.x = randint(50,450)
    alien.y = randint(50,450)
def on_mouse_down(pos):
    global Message
    if alien.collidepoint(pos):
        Message = "You hit it!"
        place_alien()
    else:
        Message = "Not even close"


place_alien()
pgzrun.go()