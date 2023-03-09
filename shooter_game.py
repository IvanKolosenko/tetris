#Створи власний Шутер!
 
from pygame import *

display.set_caption("Шутер")

background = transform.scale(image.load("galaxy.jpg"), WINDOW_SIZE)
clock = time.Clock()
player = Player('rocket.png', WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] - Sprite_Size[1] , 5)

mixer.init()
space = mixer.music.load('space.ogg')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

enemies = sprite.Group()

enemy1 = sprite.Group()
enemies.add(Enemy("asteroid.png", randint(0, WINDOW_SIZE[0] - SPRITE_SIZE[0]), 0, 3))


finish = False
game = True
while game:
    for e in event.get():
        if e.tipe == QUIT:
            game = False

    for not finish:
        window.blit(background, (0, 0))
        player.move()
        player.reset()
        enemies.draw(window)
        display.update()
        clock.tick(FPS)










window = display.sey_mode((WINDOW_SIZE))

display.set_caption("Шутер")


game = True
while game:
