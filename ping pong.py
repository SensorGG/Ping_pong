from pygame import *
screen = display.set_mode((1000 , 800))
game = True
while game:
    screen.fill(6777)
    for i in event.get():
        if i.type == QUIT:
            game = False
    time.delay(10)
    display.update()


