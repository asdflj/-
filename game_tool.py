
import random
from game_connect import Connect as C
from game_rule import Rule as R


class Tool(object):
    def fapai():
        list_size = []
        for x in range(54):
            list_size.append(x+1)
        man_list1 = []
        man_list2 = []
        man_list3 = []
        i = 54
        while i > 37:
            c = random.choice(range(i))
            man_list1.append(list_size[c])
            del list_size[c]
            i -= 1
        while i > 20:
            c = random.choice(range(i))
            man_list2.append(list_size[c])
            del list_size[c]
            i -= 1
        while i > 3:
            c = random.choice(range(i))
            man_list3.append(list_size[c])
            del list_size[c]
            i -= 1
        return man_list1, man_list2, man_list3, list_size

    def paixu(list_need):
        list_fin = sorted(list_need, reverse=True)
        return list_fin

    def fanyi(list_picture):
        dic_cards = {
            54: ('RED JOKER'), 53: ('BLACK JOKER'),
            52: ('\u2660'' 2'), 51: ('\u2663'' 2'), 50: ('\u2665'' 2'), 49: ('\u2666'' 2'),
            48: ('\u2660'' A'), 47: ('\u2663'' A'), 46: ('\u2665'' A'), 45: ('\u2666'' A'),
            44: ('\u2660'' K'), 43: ('\u2663'' K'), 42: ('\u2665'' K'), 41: ('\u2666'' K'),
            40: ('\u2660'' Q'), 39: ('\u2663'' Q'), 38: ('\u2665'' Q'), 37: ('\u2666'' Q'),
            36: ('\u2660'' J'), 35: ('\u2663'' J'), 34: ('\u2665'' J'), 33: ('\u2666'' J'),
            32: ('\u2660'' 10'), 31: ('\u2663'' 10'), 30: ('\u2665'' 10'), 29: ('\u2666'' 10'),
            28: ('\u2660'' 9'), 27: ('\u2663'' 9'), 26: ('\u2665'' 9'), 25: ('\u2666'' 9'),
            24: ('\u2660'' 8'), 23: ('\u2663'' 8'), 22: ('\u2665'' 8'), 21: ('\u2666'' 8'),
            20: ('\u2660'' 7'), 19: ('\u2663'' 7'), 18: ('\u2665'' 7'), 17: ('\u2666'' 7'),
            16: ('\u2660'' 6'), 15: ('\u2663'' 6'), 14: ('\u2665'' 6'), 13: ('\u2666'' 6'),
            12: ('\u2660'' 5'), 11: ('\u2663'' 5'), 10: ('\u2665'' 5'), 9: ('\u2666'' 5'),
            8: ('\u2660'' 4'), 7: ('\u2663'' 4'), 6: ('\u2665'' 4'), 5: ('\u2666'' 4'),
            4: ('\u2660'' 3'), 3: ('\u2663'' 3'), 2: ('\u2665'' 3'), 1: ('\u2666'' 3'),
        }
        ser_list = []
        for x in list_picture:
            ser_list.append(dic_cards[x])
        return ser_list

    def gai_1_le(pass_num, up, down, p1):
        while True:
            C.send_to_p1(R.fanyi(p1))  # 看手牌
            sy = C.sr_p1(p1)  # 得到打牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p1[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序多前少后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌行编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 必须出牌 no pass!
                    continue
                C.send_to_all("pass")
                pass_num -= 1
                return pass_num, up, down, p1  # pass
            else:
                if pass_num == 0:
                    up = daxiao_lis
                    for x in sy_fh:
                        del p1[x]
                    C.send_to_p1(R.fanyi(p1))
                    C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 1:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]
                    C.send_to_p1(R.fanyi(p1))
                    C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 2:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]
                    C.send_to_p1(R.fanyi(p1))
                    C.send_to_all(R.fanyi(lis_outparper))

                    return pass_num, up, down, p1

    def gai_2_le(pass_num, up, down, p2):
        while True:
            C.send_to_p2(R.fanyi(p2))  # 看手牌
            sy = C.sr_p2(p2)  # 得到打牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p2[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序多前少后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌行编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 必须出牌 no pass!
                    continue
                C.send_to_all("pass")
                pass_num -= 1
                return pass_num, up, down, p2  # pass
            else:
                if pass_num == 0:
                    up = daxiao_lis
                    for x in sy_fh:
                        del p2[x]
                    C.send_to_p2(R.fanyi(p2))
                    C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 1:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]
                        C.send_to_p2(R.fanyi(p2))
                        C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 2:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]
                    C.send_to_p2(R.fanyi(p2))
                    C.send_to_all(R.fanyi(lis_outparper))

                    return pass_num, up, down, p2

    def gai_3_le(pass_num, up, down, p3):
        while True:
            C.send_to_p3(R.fanyi(p3))  # 看手牌
            sy = C.sr_p3(p3)  # 得到打牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p3[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序多前少后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌行编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 必须出牌 no pass!
                    continue
                C.send_to_all("pass")
                pass_num -= 1
                return pass_num, up, down, p3  # pass
            else:
                if pass_num == 0:
                    up = daxiao_lis
                    for x in sy_fh:
                        del p3[x]
                    C.send_to_p3(R.fanyi(p3))
                    C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 1:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]
                    C.send_to_p3(R.fanyi(p3))
                    C.send_to_all(R.fanyi(lis_outparper))
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 2:
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]
                    C.send_to_p3(R.fanyi(p3))
                    C.send_to_all(R.fanyi(lis_outparper))

                    return pass_num, up, down, p3
