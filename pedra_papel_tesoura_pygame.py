from pygame import *
import sys

init()

#importanto imagens
papel_img = image.load("papel.png")
papel_img = transform.scale(papel_img, (200,200))

pedra_img = image.load("pedra.png")
pedra_img = transform.scale(pedra_img,(200,200))

tesoura_img = image.load("tesoura.png")
tesoura_img = transform.scale(tesoura_img,(200,200))


window = display.set_mode((1200,640))
running = True
clock= time.Clock()
window.fill ((6, 64, 43))


while True:
    clock.tick(60)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()



    window.blit(papel_img,(500,400))
    window.blit (pedra_img, (100,400))
    window.blit(tesoura_img, (900,400))

    
    display.update()