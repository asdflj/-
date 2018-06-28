#游戏流程类
from game_tool import Tool as T
from game_connect import Connect as C
import random
from game_room import Game


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
        L.up_date(play1_fh,play2_fh,play3_fh,dipai=[],out_poke=[],users)

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
                a = C.dz_p1('是否要地主',title,users[0])
                if a == 'y':
                    dizhu = 1
            elif x == 2:
                a = C.dz_p2('是否要地主',title,users[1])
                if a == 'y':
                    dizhu = 2
            elif x == 3:
                a = C.dz_p3('是否要地主',title,users[2])
                if a == 'y':
                    dizhu = 3
        #根据地主位置生成出牌顺序
        if dizhu == 1:
            lt = [1, 2, 3]
        elif dizhu == 2:
            lt = [2, 3, 1]
        elif dizhu == 3:
            lt = [3, 1, 2]
        #给所有玩家发送地主玩家为谁
        title = 'xszf_num'
        C.send_to_all("地主为玩家%d,"%dizhu,title,users)
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

        L.up_date(caozuo1, caozuo2, caozuo3,dipai,out_poke=[],users)
        return caozuo1, caozuo2, caozuo3

    def up_date(paly1,play2,play3,dipai=[],out_poke=[],users):
        shoupai = [paly1,play2,play3]

        shoupai_num = [len(shoupai[0]),len(shoupai[1]),len(shoupai[2])]

        update_list = [shoupai,dipai,out_poke,shoupai_num]

        title = 'up_screen'
        for y in range(3):
            sp = update_list[0][y]
            dp = update_list[1]
            op = update_list[2]
            if y ==0:
                a,b = 1,2
            elif y==1:
                a,b = 2,0
            else:
                a,b = 0,1
                #先下家后上家
            spn = [update_list[4][a],update_list[4][b]]
            update_list_child = [sp,dp,op,spn]
            #向客户端发送数据函数
            C.send_to_all(update_list_child,title,users[y])
            #title2 列表串 更新每个玩家屏幕

    def game_time_start(play1, play2, play3, lis_123,users,dipai):
        # 游戏中操作修改的对象p1,p2,p3,up,down
        # p1,p2,p3为玩家当前手牌；
        #    up为上家出牌，down为玩家出牌。判断大小用
        #    pass_num为判断pass的记录，
        #    值为0时表示此时玩家可以随意出牌
        #    值为1或2时表示此时玩家必须压牌或者pass

           
        p1 = play1
        p2 = play2
        p3 = play3
        up = []
        down = []
        pass_num = 0
        win_num = 0

        while True:  # 出牌主函数，结束返回胜者座位号
            for x in lis_123:
                if x == 1:
                    pass_num, up, down, p1 =\
                        T.gai_1_le(pass_num, up, down, p1,p2,p3,users,dipai)
                    if len(p1) == 0:#手牌为0结束游戏
                        win_num = 1
                        return win_num
                elif x == 2:
                    pass_num, up, down, p2 =\
                        T.gai_2_le(pass_num, up, down, p1,p2,p3,users,dipai)
                    if len(p2) == 0:
                        win_num = 2
                        return win_num
                elif x == 3:
                    pass_num, up, down, p3 =\
                        T.gai_3_le(pass_num, up, down, p1,p2,p3,users,dipai)
                    if len(p3) == 0:
                        win_num = 3
                        return win_num

    def end_result(king_num, win_num,users):
        title3 = 'xszf_end'
        if king_num == win_num:
            C.send_to_all("地主获胜",title3,users)
        else:
            C.send_to_all("农民获胜",title3,users)
