from game_tool import Tool

class Game_time():
    def __init__(self,room):
	self.users = room.users
	self.user1 = self.users[0].getSockfd()
	self.user2 = self.users[1].getSockfd()
	self.user3 = self.users[2].getSockfd()
    paly1,play2,play3,dipai = Tool.fapai()

    self.up_date(addr,paly1,play2,play3)

    king_num,chupai_list = self.jiaodizhu()

    paly1,play2,play3 = Tool.fendizhu(play1, play2, play3, dipai, king_num)

    win_num = self.game_time_start(play1, play2, play3,dipai, chupai_list)

    def send_all(self,list,addr):
        sockfd.send(list,addr)


    def up_date(self,addr,paly1,play2,play3,dipai=[],out_poke=[])
        shoupai = [paly1,play2,play3]

        shoupai_num = [len(shoupai[0]),len(shoupai[1]),len(shoupai[2])]

        update_list = [shoupai,out_poke,dipai,shoupai_num]
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
            self.send_all(update_list_child,addr[y])



    def jiaodizhu(self):  # 叫地主
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
        for x in lis:
            if x == 1:
                sockfd.send("是否要地主",addr[0])
                a = sockfd.recv()
                if a == 'y':
                    dizhu = 1
            elif x == 2:
                sockfd.send("是否要地主",addr[1])
                a = sockfd.recv()
                if a == 'y':
                    dizhu = 2
            elif x == 3:
                sockfd.send("是否要地主",addr[2])
                a = sockfd.recv()
                if a == 'y':
                    dizhu = 3
        #根据地主位置生成出牌顺序
        if dizhu == 1:
            lt = [1, 2, 3]
        elif dizhu == 2:
            lt = [2, 3, 1]
        elif dizhu == 3:
            lt = [3, 1, 2]

    def game_time_start(self,play1, play2, play3,dipai, chupai_list):
        p1 = play1
        p2 = play2
        p3 = play3
        dipai = dipai
        up = []
        down = []
        pass_num = 0
        win_num = 0

        while True:  # 出牌主函数，结束返回胜者座位号

            for x in chupai_list:
                self.up_date(addr,p1,p2,p3,dipai,up)
                if x == 1:
                    pass_num, up, down, p1 =\
                        self.gai_1_le(pass_num, up, down, p1,p2,p3)

                    self.up_date(addr,p1,p2,p3,dipai,up)

                    if len(p1) == 0:#手牌为0结束游戏
                        win_num = 1
                        return win_num
                elif x == 2:
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num, up, down, p2 =\
                        self.gai_2_le(pass_num, up, down, p1,p2,p3)
                    
                    self.up_date(addr,p1,p2,p3,dipai,up)

                    if len(p2) == 0:
                        win_num = 2
                        return win_num
                elif x == 3:
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num, up, down, p3 =\
                        self.gai_3_le(pass_num, up, down, p1,p2,p3)
                    
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    if len(p3) == 0:
                        win_num = 3
                        return win_num


    def gai_1_le(self,pass_num, up, down, p1,p2,p3):
    '''此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS'''
        while True:
            self.up_date(addr,p1,p2,p3,dipai,up) # 更新屏幕
            #等待用户回复出牌序列
            sy = sockfd.recv() # 得到玩家的出牌序列-------------------------------------------
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p1[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = Tool.dibanchu(lis)  # 转换为实际大小
            lis = Tool.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = Tool.chupaifanyi(lis, lis_copy)
            daxiao_lis = Tool.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                self.up_date(addr,p1,p2,p3,dipai,up)#玩家没有出牌，表示PASS 如何显示PASS
                pass_num -= 1
                return pass_num, up, down, p1  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌

                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p1

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p1
                    for x in sy_fh:
                        del p1[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)

                    return pass_num, up, down, p1#玩家出牌结束返回变量

    def gai_2_le(self,pass_num, up, down, p1,p2,p3):
    '''此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS'''
        while True:
            self.up_date(addr,p1,p2,p3,dipai,up) # 更新屏幕
            #等待用户回复出牌序列
            sy = sockfd.recv()  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p2[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = Tool.dibanchu(lis)  # 转换为实际大小
            lis = Tool.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = Tool.chupaifanyi(lis, lis_copy)
            daxiao_lis = Tool.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                self.up_date(addr,p1,p2,p3,dipai,up)#玩家没有出牌，表示PASS
                pass_num -= 1
                return pass_num, up, down, p2  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌

                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p2

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p2
                    for x in sy_fh:
                        del p2[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)

                    return pass_num, up, down, p2#玩家出牌结束返回变量

    def gai_3_le(self,pass_num, up, down, p1,p2,p3):
    '''此类函数处理玩家发牌中，是否规范，是否合法，是否为PASS'''
        while True:
            self.up_date(addr,p1,p2,p3,dipai,up) # 更新屏幕
            #等待用户回复出牌序列
            sy = sockfd.recv()  # 得到玩家的出牌序列
            sy_fh = sorted(sy, reverse=True)  # 排序
            lis = []
            for x in sy:
                s = p3[x]
                lis.append(s)
            lis_copy = lis  # 备份
            lis = Tool.dibanchu(lis)  # 转换为实际大小
            lis = Tool.many_first(lis)  # 排序数量多牌在前数量少的牌在后
            lis_outparper = Tool.chupaifanyi(lis, lis_copy)
            daxiao_lis = Tool.fanhui_xulie(lis)  # 拿到相应牌值编号
            if daxiao_lis[0] == 100:
                continue  # 不符合规则，重新出牌
            if daxiao_lis[0] == 4:
                if pass_num == 0:
                      # 此时必须出牌不能PASS，可以随意出
                    continue
                self.up_date(addr,p1,p2,p3,dipai,up)#玩家没有出牌，表示PASS
                pass_num -= 1
                return pass_num, up, down, p3  # pass
            else:
                if pass_num == 0:#随意出牌的情况
                    up = daxiao_lis
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌

                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 1:#必须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 1
                        continue
                    if down[0] == 4:
                        pass_num = 0
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)
                    pass_num = 2
                    return pass_num, up, down, p3

                elif pass_num == 2:#须大于上家才能出的情况
                    down = daxiao_lis
                    up, down = Tool.bidaxiao(up, down)
                    if down[-1] == 50:
                        pass_num == 2
                        continue
                    if down[0] == 4:
                        pass_num = 1
                        return pass_num, up, down, p3
                    for x in sy_fh:
                        del p3[x]#出牌成功，删除手中打出的牌
                    
                    #给所有玩家展示打出的牌
                    self.up_date(addr,p1,p2,p3,dipai,up)

                    return pass_num, up, down, p3#玩家出牌结束返回变量
