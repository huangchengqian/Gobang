import pygame as pg

from game.game import check, set_check
import util.constant as cons

def ui_init():
    pg.init()
    screen = pg.display.set_mode((cons.UI_WIDTH, cons.UI_HEIGHT))
    clock = pg.time.Clock()

    background = pg.image.load("./resource/img/checkerboard.png").convert_alpha()
    black = pg.image.load("./resource/img/black.png").convert_alpha()
    white = pg.image.load("./resource/img/white.png").convert_alpha()
    font = pg.font.Font('./resource/font/SIMHEI.TTF', 100)

    pg.display.set_caption("五子棋")

    object = []

    # 落子顺序判断
    cur_player = [black, white]
    flag = False
    play = False

    going = True
    while going:
        a, b = 0, 0
        screen.blit(background, (0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE:
                going = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                a, b = round((pos[0] - cons.MARGIN_SIZE) / cons.GRIND_SIZE), round((pos[1] - cons.MARGIN_SIZE) / cons.GRIND_SIZE)
                if a < 0 or b < 0 or a >= cons.BOARD_LINE or b >= cons.BOARD_LINE or not set_check(a, b, cur_player[flag]):
                    continue
                object.append([cur_player[flag], [a * cons.GRIND_SIZE + cons.MARGIN_SIZE, b * cons.GRIND_SIZE + cons.MARGIN_SIZE]])
                flag = not flag
                play = True
                
        for o in object:
            screen.blit(o[0], o[1])

        if play and check(a, b, o[0]):
            text = '黑棋赢辣！'
            if o[0] == white:
                text = '白棋赢辣！'
            text = font.render(text, True, (0, 0, 255), (0, 255, 0))
            screen.blit(text, (300, 400))
            going = False
            
        clock.tick(60)
        pg.display.update()
        play = False
        if not going:
            pg.time.wait(10000)

    pg.quit()