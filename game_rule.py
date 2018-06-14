#出牌规则类函数
class Rule(object):
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

    def dibanchu(lis):
        #将牌转换为1-K
        lis_diban = []
        for x in lis:
            if x == 54:
                lis_diban.append(15)
            else:
                a = (x-1) // 4 + 1
                lis_diban.append(a)
        return lis_diban

    def chupaifanyi(lis_diban, lis_fanyi):
           #打出的牌转换器
        lis_666 = []
        for x in lis_diban:
            for y in lis_fanyi:
                if (y-1)//4+1 == x:
                    lis_666.append(y)
                    lis_fanyi.remove(y)
        return lis_666

    def many_first(lis):  # 出牌排序
        count1 = []
        count2 = []
        count3 = []
        count4 = []
        for x in lis:
            if lis.count(x) == 4:
                count4.append(x)
            elif lis.count(x) == 3:
                count3.append(x)
            elif lis.count(x) == 2:
                count2.append(x)
            else:
                count1.append(x)
        count1 = sorted(count1, reverse=True)
        count2 = sorted(count2, reverse=True)
        count3 = sorted(count3, reverse=True)
        count4 = sorted(count4, reverse=True)
        zong = count4+count3+count2+count1
        return zong

    def fanhui_xulie(lis):  
    # 判断出牌是否符合规则，不符合返回，玩家PASS时返回空列表
        def much_first(lis):
            much = []
            count1 = []
            count2 = []
            count3 = []
            count4 = []
            for x in lis:
                if lis.count(x) == 4:
                    count4.append(x)
                elif lis.count(x) == 3:
                    count3.append(x)
                elif lis.count(x) == 2:
                    count2.append(x)
                else:
                    count1.append(x)
            count1 = sorted(count1, reverse=True)
            count2 = sorted(count2, reverse=True)
            count3 = sorted(count3, reverse=True)
            count4 = sorted(count4, reverse=True)

            return count1, count2, count3, count4

        def leixing(lis):  # 牌形选择，出牌中相同牌最大数量
            '''
            1为单牌类型（单张或单顺）
            2为对子类型（单对或连对）
            3为飞机类型
            4为炸弹
            '''
            b = 0
            if lis != []:
                for x in lis:
                    a = lis.count(x)
                    if a > b:
                        b = a
            return b

        def feiji(lis):  # 飞机类型判断
            pt = []
            count1, count2, count3, count4 = much_first(lis)
            p3, p2, p1 = len(count3), len(count2), len(count1)
            if count3[0]-count3[-1]+1 == len(count3)//3:
                # fly不带
                if p2 == 0 and p1 == 0:
                    pt += [1, 3, 3, 1, p3//3]
                    return pt
                # fly带单
                elif p2 == 0 and p1 == p3//3:
                    s = count3+count1
                    pt += [1, 3, 3, 2, p3//3, s[0]]
                    return pt
                elif p2+p1 == p3//3:
                    s = count3+count2+count1
                    pt += [1, 3, 3, 2, p3//3, s[0]]
                    return pt
                # fly带双
                elif p1 == 0 and p2//2 == p3//3:
                    s = count3+count2
                    pt += [1, 3, 3, 3, p3//3, s[0]]
                    return pt
            return pt

        def putong_panduan(lis):  # 牌型判断
            pt = []
            #pt[-1]为大小
            b = leixing(lis)
            if b == 1:
                if len(lis) == 1:
                    pt += [1, 1, 1, lis[0]]
                    return pt
                elif len(lis) >= 5:
                    if lis[0]-lis[-1]+1 == len(lis):
                        if lis[0] <= 12:
                            pt += [1, 1, len(lis), lis[0]]
                            return pt  # 单顺
            elif b == 2:
                if len(lis) == 2:
                    pt += [1, 2, 2, lis[0]]
                    return pt  # 单对
                    # 加连对判断
                elif len(lis) >= 6 and len(lis) % 2 == 0\
                        and lis[0]-lis[-1]+1 == len(lis)//2:
                    pt += [1, 2, len(lis), lis[0]]
                    return pt  # 连对
            elif b == 3:
                if len(lis) == 3:
                    pt += [1, 3, 1, lis[0]]
                    return pt  # 三不带
                elif len(lis) == 4:
                    pt += [1, 3, 2, 1, lis[0]]
                    return pt  # 三带一
                elif len(lis) == 5:
                    pt += [1, 3, 2, 2, lis[0]]
                    return pt  # 三带二
                else:
                    return feiji(lis)
            elif b == 4:
                if len(lis) == 6:
                    pt += [1, 4, 1, lis[0]]
                    return pt
                elif len(lis) == 8:
                    pt += [1, 4, 2, lis[0]]
                    return pt
            pt += [100]  # 不符合规则返回100
            return pt

        daxiao_list = []
        if len(lis) == 0:
            daxiao_list.append(4)  # pass 信号
            return daxiao_list
        if len(lis) == 2 and lis[0] == lis[1] == 14:
            daxiao_list.append(3)
            # 王炸
            return daxiao_list
        elif len(lis) == 4 and leixing(lis) == 4:
            daxiao_list.append(2)
            daxiao_list.append(lis[0])
            # 炸弹
            return daxiao_list
        else:
            daxiao_list = putong_panduan(lis)
            return daxiao_list

    def bidaxiao(up, down):
        pt = [50]
        if len(up) == 0:
            up = down
        else:
            if down[0] > up[0]:
                up = down
            elif down[0] < up[0]:
                return up, pt  # 比较失败返回５０

            elif down[0] == up[0]:
                if up[0] == 2:
                    if down[1] > up[1]:
                        up = down
                    else:
                        return up, pt
                if up[0] == 1:
                    if down[0:len(down)-1:1] == up[0:len(down)-1:1]:
                        if down[-1] > up[-1]:
                            up = down
                        else:
                            return up, pt
                    else:
                        return up, pt
            else:
                return up, pt

        return up, down
