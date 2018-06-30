'''游戏流程类'''
from game_tool import Tool as T
from game_connect import Connect as C
import random


class Liucheng(object):

    def fenpai(users):
        # 获得底牌和分牌
        play1, play2, play3, dipai = T.fapai()
        # 排序并转换为图形
        play1_fh = T.paixu(play1)
        play2_fh = T.paixu(play2)
        play3_fh = T.paixu(play3)
        dipai_fh = T.paixu(dipai)
        #分别将数据发送给玩家
        T.up_date(play1_fh,play2_fh,play3_fh,users,dipai=[],out_poke=[])
        return play1_fh, play2_fh, play3_fh, dipai_fh

    def jiaodizhu(dipai,users):  # 叫地主
        #随机生成先叫地主的人，生成叫地主顺序列表
        three = random.choice([1, 2, 3])
        if three == 1:
            lis = [1, 2, 3, 1]
            dizhu = 1
        elif three == 2:
            lis = [2, 3, 1, 2]
            dizhu = 2
        elif three == 3:
            lis = [3, 1, 2, 3]
            dizhu = 3
        #根据顺序由每位玩家叫地主
        title = 'xszf_jdz' #显示字符
        for x in lis:
            if x == 1:
                a = C.dz_p1('Be a king?',title,users[0])
                if a == 'y':
                    dizhu = 1
                    C.send_msg_all('play1 say yes','msg',users)
                else:
                    C.send_msg_all('play1 say no','msg',users)
            elif x == 2:
                a = C.dz_p2('Be a king?',title,users[1])
                if a == 'y':
                    dizhu = 2
                    C.send_msg_all('play2 say yes','msg',users)
                else:
                    C.send_msg_all('play2 say no','msg',users)
            elif x == 3:
                a = C.dz_p3('Be a king?',title,users[2])
                if a == 'y':
                    dizhu = 3
                    C.send_msg_all('play3 say yes','msg',users)
                else:
                    C.send_msg_all('play3 say no','msg',users)
        #根据地主位置生成出牌顺序
        if dizhu == 1:
            lt = [1, 2, 3]
        elif dizhu == 2:
            lt = [2, 3, 1]
        elif dizhu == 3:
            lt = [3, 1, 2]
        
        #给所有玩家发送地主玩家为谁
        title1 = 'xszf_num'
        C.send_msg_all("The king is %d" % dizhu,title1,users)
        return dizhu, lt

    def fendizhu(play1, play2, play3, dipai, king_num,users):  
    # 根据结果分牌
        if king_num == 1:
            dizhu1 = dipai+play1
            caozuo1 = dizhu1
            caozuo2 = play2
            caozuo3 = play3
        elif king_num == 2:
            dizhu2 = dipai+play2
            caozuo1 = play1
            caozuo2 = dizhu2
            caozuo3 = play3
        elif king_num == 3:
            dizhu3 = dipai+play3
            caozuo1 = play1
            caozuo2 = play2
            caozuo3 = dizhu3

        caozuo1 = T.paixu(caozuo1)
        caozuo2 = T.paixu(caozuo2)
        caozuo3 = T.paixu(caozuo3)

        T.up_date(caozuo1, caozuo2, caozuo3,users,dipai,out_poke=[])
        return caozuo1, caozuo2, caozuo3

    def game_time_start(play1, play2, play3, lis_123,dipai,users):
        # 游戏中操作修改的对象p1,p2,p3,up,down
        '''p1,p2,p3为玩家当前手牌；
           up为上家出牌，down为玩家出牌。判断大小用
           pass_num为判断pass的记录，
           值为0时表示此时玩家可以随意出牌
           值为1或2时表示此时玩家必须压牌或者pass

           '''
        p1 = play1
        p2 = play2
        p3 = play3
        up = []
        out_up = []
        down = []
        pass_num = 0
        win_num = 0

        while True:  # 出牌主函数，结束返回胜者座位号
            for x in lis_123:
                if x == 1:
                    pass_num, up,out_up, down, p1 =\
                        T.gai_1_le(pass_num, up,out_up,down, p1,p2,p3,users,dipai)
                    if len(p1) == 0:#手牌为0结束游戏
                        win_num = 1
                        return win_num
                elif x == 2:
                    pass_num, up,out_up , down, p2=\
                        T.gai_2_le(pass_num, up,out_up, down, p1,p2,p3,users,dipai)
                    if len(p2) == 0:
                        win_num = 2
                        return win_num
                elif x == 3:
                    pass_num, up,out_up, down, p3 =\
                        T.gai_3_le(pass_num, up,out_up, down, p1,p2,p3,users,dipai)
                    if len(p3) == 0:
                        win_num = 3
                        return win_num

    def end_result(king_num, win_num,users):
        if king_num == win_num:

            C.send_msg_all("King Win",'xszf_end',users)
        else:
            C.send_msg_all("People Win",'xszf_end',users)
