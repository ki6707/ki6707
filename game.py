from pygame import*
size=(500,400)
screen=display.set_mode(size)
while True:
    for i in event.get():
        if i.type==MOUSEBUTTONUP:
            pos=mouse.get_pos()
            col=(0,255,255)
            draw.circle(
                screen,col,pos,20,5)
            display.update()