'''此文件为数传输类，传输对象都为列表形式'''
#导入套接字，导入每位玩家的通讯地址

def sendRoomMessage(msg,title,user=None):
    for i in self.users:
        if i is user:
            send_msg = i.convert(msg,title)  # 把消息转换成协议格式
            i.sendMessage(send_msg)


class Connect(object):



    
    def send_to_p1(lis,title1,users):
        sendRoomMessage(lis,title,user=users[0])
        #s.send(lis,addr)
        #play1手牌

    def send_to_p2(lis,title1,users):
        sendRoomMessage(lis,title,user=users[1])
        #play2手牌

    def send_to_p3(lis,title1,users):
        sendRoomMessage(lis,title,user=users[2])
        #play3手牌
    #以上为玩家手牌更新传输，用户界面显示位置为（1）
    
    def send_to_all(lis,title,user):

        sendRoomMessage(lis,title,user)#title = 'up_screen'
        

    def dz_p1(s,title3,user):#title = 'xszf' (显示字符)
        sendRoomMessage(s,title3,user)
        re = user.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play1是否要地主？y/n"
        #接收用户返回数据
        return re['data']

    def dz_p2(s,title3,user):#title = 'xszf' (显示字符)
        sendRoomMessage(s,title3,user)
        re = user.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play2是否要地主？y/n"
        #接收用户返回数据
        return re['data']

    def dz_p3(s,title3,user):#title = 'xszf' (显示字符)
        sendRoomMessage(s,title3,user)
        re = user.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play3是否要地主？y/n"
        #接收用户返回数据
        return re['data'] 
    #以上为判断地主传输，用户界面显示位置为（3）
    
    def sr_p1():
        li = []
        while True:
            sd = user.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            sd=sd['data']
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            if sd in li:
                li.remove(x)
                continue
            li.append(sd)
            if sd == 40:
                li = []
                break
        return li

    def sr_p2():
        li = []
        while True:
            sd = user.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            sd=sd['data']
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            if sd in li:
                li.remove(x)
                continue
            li.append(sd)
            if sd == 40:
                li = []
                break

        return li

    def sr_p3():
        li = []
        while True:
            sd = user.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            sd=sd['data']
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            if sd > (len(lis)-1) and sd != 20:
                #点击没有牌的位置无效
                continue
            if sd == 20:  # 20为提交指令
                break
            if sd in li:
                li.remove(x)
                continue
            li.append(sd)
            if sd == 40:
                li = []
                break
        return li
    #以上为用户出牌接收函数，接收到20信号时表示用户提交指令
