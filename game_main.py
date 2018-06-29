

from game_liucheng import Liucheng as L
from game_tool import Tool as T
import time

def main(users):
    #完成首次发牌，生成三张底牌，并且将发牌的结果给玩家

    play1, play2, play3, dipai = L.fenpai(users)

    king_num, lis_123 = L.jiaodizhu(dipai,users)

    play1, play2, play3 = L.fendizhu(play1, play2, play3, dipai, king_num,users)

    win_num = L.game_time_start(play1, play2, play3, lis_123,dipai,users)

    L.end_result(king_num, win_num,users)


