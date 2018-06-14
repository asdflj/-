'''此文件为数传输类，传输对象都为列表形式'''
#导入套接字，导入每位玩家的通讯地址
class Connect(object):
    
    def send_to_p1(lis,addr_1):
        #s.send(lis,addr)
        #play1手牌

    def send_to_p2(lis,addr_2):
        #play2手牌

    def send_to_p3(lis,addr_3):
        #play3手牌
    #以上为玩家手牌更新传输，用户界面显示位置为（1）
    
    def send_to_all(s,addr_all):
        #谁是地主，底牌公布，出牌公布，游戏结果公布
        #用户界面显示位置为（2）

    def dz_p1(addr_1):
        #发送："play1是否要地主？y/n"
        #接收用户返回数据
        return 

    def dz_p2(addr_2):
        #发送："play2是否要地主？y/n"
        #接收用户返回数据
        return 

    def dz_p3(addr_3):
        #发送："play3是否要地主？y/n"
        #接收用户返回数据
        return 
    #以上为判断地主传输，用户界面显示位置为（3）
    
    def sr_p1(addr_1):
        li = []
        while True:
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
        return li

    def sr_p2(addr_2):
        li = []
        while True:
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
        return li

    def sr_p3(addr_3):
        li = []
        while True:
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
        return li
    #以上为用户出牌接收函数，接收到20信号时表示用户提交指令
