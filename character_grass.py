from pico2d import *
import math

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')



while 1:

    x = 0
    y = 90
    pi = 3.141592
    rad = 3*pi/2

    while x<780:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        update_canvas()
        x += 9
        delay(0.01)

    while y<550:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        y += 9
        delay(0.01)


    while 20<x:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        x -= 9
        delay(0.01)

    while 90<y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        y -= 9
        delay(0.01)


    while rad> -pi/2:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(230*math.cos(rad)+400, 230*math.sin(rad)+345)
        update_canvas()
        rad-=0.01
        delay(0.01)


close_canvas()



# fill here
