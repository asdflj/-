def sendRoomMessage(msg,title,user):
    send_msg = user.convert(msg,title)  # 把消息转换成协议格式
    user.sendMessage(send_msg)



class Connect(object):
    def send_to_all(lis,title,addr):
        sendRoomMessage(repr(lis),title,addr)
        # print(lis,title,user)#title = 'up_screen'

    def dz_p1(s,title3,addr):#title = 'xszf_jdz' (显示字符)
        sendRoomMessage(s,title3,addr)
        re = addr.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play1是否要地主？y/n"
        #接收用户返回数据
        return re['data']

    def dz_p2(s,title3,addr):#title = 'xszf_jdz' (显示字符)
        sendRoomMessage(s,title3,addr)
        re = addr.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play1是否要地主？y/n"
        #接收用户返回数据
        return re['data']

    def dz_p3(s,title3,addr):#title = 'xszf_jdz' (显示字符)
        sendRoomMessage(s,title3,addr)
        re = addr.getMessage(convertToDict=True)#用户点击 叫地主 返回字符 'y'
        #发送："play1是否要地主？y/n"
        #接收用户返回数据
        return re['data']
    
    
    def send_msg_all(s,title,users):
        for x in users:
            sendRoomMessage(s,title,x)



    def send_to_one(s,title,addr):
        sendRoomMessage(s,title,addr)

    
        

    #以上为判断地主传输，用户界面显示位置为（3）
    
    def sr_p1(lis,addr):
        li = []
        while True:
            sd = addr.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            sd=int(sd['data'])
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

    def sr_p2(lis,addr):
        li = []
        while True:
            
            sd = addr.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            sd=int(sd['data'])
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

    def sr_p3(lis,addr):
        li = []
        while True:
            
            sd = addr.getMessage(convertToDict=True)#出牌按钮 对应返回 20，直接点提交 为PASS请求
            #接收用户返回数据，并添加为列表序列
            #用户点击相应位置返回0-19数字，出牌按钮对应20数字
            sd=int(sd['data'])
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
