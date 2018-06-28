

from game_liucheng import Liucheng as L
from game_tool import Tool as T
import time

def main(users):
    #完成首次发牌，生成三张底牌，并且将发牌的结果给玩家
    play1, play2, play3, dipai = L.fenpai(users)
    #完成分地主流程，玩家返回'Y'表示叫地主，其他则为不叫
    # king_num为最终地主玩家的玩家号
    # 列表lis_123为出牌阶段地主先发牌的顺序列表

    king_num, lis_123 = L.jiaodizhu(dipai,users)

    time.sleep(2)

 #根据地主结果，从新发送玩家手牌
    play1, play2, play3 = L.fendizhu(play1, play2, play3, dipai, king_num,users)
 #开始出牌阶段，如果某玩家手牌打完，则返回win_num，值为出完玩家的编号
    win_num = L.game_time_start(play1, play2, play3, lis_123,users,dipai)
 #判断地主编号与胜利玩家编号是否一致，来判断地主获胜或者农民获胜，并且游戏结束
    L.end_result(king_num, win_num,users)


