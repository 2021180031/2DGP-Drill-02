from pico2d import *
import math

# 초기화
open_canvas(800, 600)
character = load_image('character.png')
grass = load_image('grass.png')

def draw_character(x, y):
    """화면을 지우고 잔디와 캐릭터를 그립니다."""
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    """캐릭터가 사각형 경로로 움직이도록 합니다."""
    print("사각형 움직임 시작")
    # 아래쪽 가장자리: 오른쪽으로 이동
    for x in range(50, 751, 10):
        draw_character(x, 90)
    # 오른쪽 가장자리: 위로 이동
    for y in range(90, 551, 10):
        draw_character(750, y)
    # 위쪽 가장자리: 왼쪽으로 이동
    for x in range(750, 49, -10):
        draw_character(x, 550)
    # 왼쪽 가장자리: 아래로 이동
    for y in range(550, 89, -10):
        draw_character(50, y)

def move_circle():
    """캐릭터가 원형 경로로 움직이도록 합니다."""
    print("원형 움직임 시작")
    cx, cy, r = 400, 300, 200  # 중심 (x, y)와 반지름
    for deg in range(-90, 271, 5):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_character(x, y)

# 메인 루프
while True:
    move_rectangle()
    move_circle()

close_canvas()

