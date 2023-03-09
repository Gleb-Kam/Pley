#Створи власний Шутер!

from pygame import *
#WINDOW_SIZE = (700, 500)


#Window = display.set_mode(WINDOW_SIZE)
display.set_caption("Шутер")
baskground = transform.scale(image.load("galexy.jpn"), WINDOW_SIZE)
player = Player("rokcet.png", WINDOW_SIZE[0] / 2, WINDOW_SIZE[], 5)

mixer.init()
mixer.music.load("space.ogg")
mixer.music.set_volume(0.1)
music.music.pley()


clock = time.Cloke()
finish = False
game = True
while game:
    for e in event.get():
        if e.tyre == QUIT:
            game = False

    it not finish:
        window.blit(background, (0, 0))


        display.undate()
        clock.tick(FPS)
