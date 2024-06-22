
import util.constant as cons

# 浅拷贝创建二维列表引发的惨案
# board = [[' '] * cons.BOARD_LINE] * cons.BOARD_LINE

board = [[' '] * cons.BOARD_LINE for _ in range(cons.BOARD_LINE)]


def set_check(x, y, color):
    if board[x][y] != ' ':
        return False
    else:
        board[x][y] = color
        return True
    

# 落子后检查胜利条件
def check(x, y, color):
    return check_line(x, y, color) or check_inline(x, y, color)
 

def check_line(x, y, color):
    count = 0
    cur = x
    while cur >= 0 and board[cur][y] == color:
        count = count + 1
        cur = cur - 1
    cur = x + 1
    while cur < cons.BOARD_LINE and board[cur][y] == color:
        count = count + 1
        cur = cur + 1

    if count >= cons.WIN_NUM:
        return True
    
    cur = y
    count = 0
    while cur >= 0 and board[x][cur] == color:
        count = count + 1
        cur = cur - 1
    cur = y + 1
    while cur < cons.BOARD_LINE and board[x][cur] == color:
        count = count + 1
        cur = cur + 1

    if count >= cons.WIN_NUM:
        return True
    
    return False

def check_inline(x, y, color):
    count = 0
    cur_x, cur_y = x - 1, y - 1
    while cur_x >= 0 and cur_y >= 0 and board[cur_x][cur_y] == color:
        count = count + 1
        cur_x, cur_y = cur_x - 1, cur_y - 1
    cur_x, cur_y = x, y
    while cur_x < cons.BOARD_LINE and cur_y < cons.BOARD_LINE and board[cur_x][cur_y] == color:
        count = count + 1
        cur_x, cur_y = cur_x + 1, cur_y + 1

    if count >= cons.WIN_NUM:
        return True
    
    count = 0
    cur_x, cur_y = x + 1, y - 1
    while cur_x < cons.BOARD_LINE and cur_y >= 0 and board[cur_x][cur_y] == color:
        count = count + 1
        cur_x, cur_y = cur_x + 1, cur_y - 1
    cur_x, cur_y = x, y
    while cur_x >= 0 and cur_y < cons.BOARD_LINE and board[cur_x][cur_y] == color:
        count = count + 1
        cur_x, cur_y = cur_x - 1, cur_y + 1

    if count >= cons.WIN_NUM:
        return True
    
    return False