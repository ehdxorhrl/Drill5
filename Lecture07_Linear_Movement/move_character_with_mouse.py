from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')

def draw_move():
    # fill here
    global TUK_ground, character, arrow, frame, x, y, fx, fy
    fx = random.randint(0, TUK_WIDTH)
    fy = random.randint(0, TUK_HEIGHT)
    x1, y1 = x, y  # -100, -100
    x2, y2 = fx, fy

    for i in range(0, 300+1, 3):
        t = i / 300
        x = (1 - t) * x1 + t * x2
        y = (1 - t) * y1 + t * y2
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        arrow.clip_draw(0, 0, 50, 50, x2, y2)
        if x1 < x2:
            character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        else:
            character.clip_composite_draw(frame * 100, 100 * 1, 100, 100, 0, 'h', x, y, 100, 100)
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.01)

    x = fx
    y = fy


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
fx, fy = 0, 0
frame = 0

while running:
    draw_move()
close_canvas()




