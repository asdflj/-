#工具类函数
import random
from game_connect import Connect as C
from game_rule import Rule as R



class Tool(object):
    def fapai():
        #随机发牌函数
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

    def gai_1_le(pass_num, up, down, p1,p2,p3,users,dipai):
        #此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS
        while True:
            L.up_date(p1,p2,p3,dipai,up,users)  # 看手牌
            sy = C.sr_p1(users)  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p1[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                title3 = 'xszf_pass'    
                C.send_to_all("pass",title3,users)#玩家没有出牌，表示PASS
                pass_num -= 1
                return pass_num, up, down, p1  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)

                    return pass_num, up, down, p1#玩家出牌结束返回变量
    #参照1注释               
    def gai_2_le(pass_num, up, down, p1,p2,p3,users,dipai):
        #此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS
        while True:
            L.up_date(p1,p2,p3,dipai,up,users)  # 看手牌
            sy = C.sr_p2(users)  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p3[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                title3 = 'xszf_pass'    
                C.send_to_all("pass",title3,users)#玩家没有出牌，表示PASS
                pass_num -= 1
                return pass_num, up, down, p2  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)

                    return pass_num, up, down, p2#玩家出牌结束返回变量
    #参照1注释
    def gai_3_le(pass_num, up, down, p1,p2,p3,users,dipai):
        #此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS
        while True:
            L.up_date(p1,p2,p3,dipai,up,users)  # 看手牌
            sy = C.sr_p3(users)  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p3[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                title3 = 'xszf_pass'    
                C.send_to_all("pass",title3,users)#玩家没有出牌，表示PASS
                pass_num -= 1
                return pass_num, up, down, p3  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    L.up_date(p1,p2,p3,dipai,up,users)

                    return pass_num, up, down, p3#玩家出牌结束返回变量
