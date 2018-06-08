from game_tool import Tool as T
from game_connect import Connect as C

class Liucheng(object):

    def fenpai():
        #获得底牌和分牌
        paly1, paly2, paly3, dipai = T.fapai()
        #初始化排序
        paly1_fh = T.paixu(paly1)
        paly2_fh = T.paixu(paly2)
        paly3_fh = T.paixu(paly3)
        dipai_fh = T.paixu(dipai)

        C.send_to_p1(T.fanyi(paly1_fh))
        C.send_to_p2(T.fanyi(paly2_fh))
        C.send_to_p3(T.fanyi(paly3_fh))
        
        return paly1_fh, paly2_fh, paly3_fh, dipai_fh

    def jiaodizhu():#叫地主
        three = random.choice([1,2,3])
        if three == 1:
            lis = [1,2,3,1]
            dizhu=1
        elif three == 2:
            lis = [2,3,1,2]
            dizhu=2
        elif three == 3:
            lis = [3,1,2,3]
            dizhu=3
        for x in lis:
            if x == 1:
                C.dz_p1()
                if back == 'y':
                    dizhu=1
            elif x == 2:
                C.dz_p2()
                if back == 'y':
                    dizhu=2
            elif x == 3:
                C.dz_p3()
                if back == 'y':
                    dizhu=3
        lis_fh = lis[0:len(lis):1]

        C.send_to_all("地主为玩家%d"%dizhu)
        #to all
        return dizhu lis_fh

    def fendizhu(paly1, paly2, paly3, dipai,king_num):#根据结果分牌
        if king_num == 1:
            dizhu1 = dipai+paly1
            caozuo1 = dizhu1
            caozuo2 = paly2
            caozuo3 = paly3
        elif king_num == 2:
            dizhu2 = dipai+paly2
            caozuo1 = paly1
            caozuo2 = dizhu2
            caozuo3 = paly3
        elif king_num == 3:
            dizhu3 = dipai+paly3
            caozuo1 = paly1
            caozuo2 = paly2
            caozuo3 = dizhu3

        caozuo1 = T.paixu(caozuo1)
        caozuo2 = T.paixu(caozuo2)
        caozuo3 = T.paixu(caozuo3)

        C.send_to_p1(T.fanyi(caozuo1))
        C.send_to_p2(T.fanyi(caozuo2))
        C.send_to_p3(T.fanyi(caozuo3))
        return caozuo1,caozuo2,caozuo3

    def game_time_start(play1,play2,play3,lis_123):
        #游戏中操作修改的对象p1,p2,p3,up,down
        p1=play1
        p2=play2
        p3=play3
        up=[]
        down=[]
        pass_num=2
        win_num=0

        while True:#出牌主函数，结束返回胜者座位号
            for x in lis_123:
                if x ==1:
                    pass_num,up,down,p1=\
                    T.gai_1_le(pass_num,up,down,p1)
                    if len(p1)==0:
                        win_num=1
                        return win_num 
                elif x ==2:
                    pass_num,up,down,p2=\
                    gai_2_le(pass_num,up,down,p2)
                    if len(p2)==0:
                        win_num=2
                        return win_num 
                elif x ==3:
                    pass_num,up,down,p3=\
                    gai_3_le(pass_num,up,down,p3)
                    if len(p3)==0:
                        win_num=3
                        return win_num 
    def end_result(king_num,win_num):
        if king_num == win_num:
            C.send_to_all("地主获胜")
        else:
            C.send_to_all("农民获胜")












            # for x in lis_123:
            #     if x ==1:
            #         while True:
            #             T.gaiwole(pass_num,up,down,p1,p2,p3)
            #         if len(p1)==0 or len(p2)==0 or len(p3)==0:
            #             break
            #     elif x ==2:
            #         while True:
            #             T.gaiwole()
            #         if len(p1)==0 or len(p2)==0 or len(p3)==0:
            #             break
            #     elif x ==3:
            #         while True:
            #             T.gaiwole()
            #         if len(p1)==0 or len(p2)==0 or len(p3)==0:
            #             break
            # if len(p1)==0 or len(p2)==0 or len(p3)==0:
            #     if len(p1)==0:
            #         win_num=1
            #         return win_num
            #     if len(p2)==0:
            #         win_num=2
            #         return win_num
            #     if len(p3)==0:
            #         win_num=3
            #         return win_num