'''工具类函数'''
import random
from game_connect import Connect as C
from game_rule import Rule as R


class Tool(object):
    def up_date(paly1,play2,play3,users,dipai=[],out_poke=[]):
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
            spn = [update_list[3][a],update_list[3][b]]
            update_list_child = [sp,dp,op,spn]
            #向客户端发送数据函数
            C.send_to_all(update_list_child,title,users[y])
            #title2 列表串 更新每个玩家屏幕
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
        while True:
            R.up_date(p1,p2,p3,users,dipai,up)  # 看手牌
            title = 'start'
            s = '请玩家1出牌'
            C.send_to_one(s,title,users[0])
            sy = C.sr_p1(p1,users[0])  # 得到玩家的出牌序列
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
                C.send_to_one('出牌不符合规则','no',users[0])
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    C.send_to_one('出牌不符合规则','no',users[0])
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
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[0])
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        C.send_to_one('出牌不符合规则','no',users[0])
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[0])
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        C.send_to_one('出牌不符合规则','no',users[0])
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[0])

                    return pass_num, up, down, p1#玩家出牌结束返回变量
    #参照1注释               
    def gai_2_le(pass_num, up, down, p1,p2,p3,users,dipai):
        while True:
            R.up_date(p1,p2,p3,users,dipai,up)
            title = 'start'
            s = '请玩家2出牌'
            C.send_to_one(s,title,users[1])
            sy = C.sr_p2(p2,users[1])  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p2[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = R.dibanchu(lis)  # 转换为实际大小
            lis = R.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = R.chupaifanyi(lis, lis_copy)
            daxiao_lis = R.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0]== 100: 
                C.send_to_one('出牌不符合规则','no',users[1])
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                    C.send_to_one('出牌不符合规则','no',users[1])
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
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[1])
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        C.send_to_one('出牌不符合规则','no',users[1])
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[1])
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        C.send_to_one('出牌不符合规则','no',users[1])
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[1])

                    return pass_num, up, down, p2#玩家出牌结束返回变量
    #参照1注释
    def gai_3_le(pass_num, up, down, p1,p2,p3,users,dipai):
        while True:
            R.up_date(p1,p2,p3,users,dipai,up)
            title = 'start'
            s = '请玩家3出牌'
            C.send_to_one(s,title,users[0])
            sy = C.sr_p3(p3,users[2])  # 得到玩家的出牌序列
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
            if daxiao_lis[0]== 100: 
                C.send_to_one('出牌不符合规则','no',users[2])
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                    C.send_to_one('出牌不符合规则','no',users[2])
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
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[2])
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        C.send_to_one('出牌不符合规则','no',users[2])
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[2])
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = R.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        C.send_to_one('出牌不符合规则','no',users[2])
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    R.up_date(p1,p2,p3,users,dipai,up)
                    C.send_to_one('出牌成功','ok',users[2])

                    return pass_num, up, down, p3#玩家出牌结束返回变量
