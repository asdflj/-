
class Connect(object):
    def send_to_p1(lis):
        print("play1手牌为：", lis)

    def send_to_p2(lis):
        print("play2手牌为：", lis)

    def send_to_p3(lis):
        print("play3手牌为：", lis)

    def send_to_all(s):
        print(s)

    def dz_p1():
        print("play1是否要地主？y/n")
        c = input("请输入：")
        return c

    def dz_p2():
        print("play2是否要地主？y/n")
        c = input("请输入：")
        return c

    def dz_p3():
        print("play3是否要地主？y/n")
        c = input("请输入：")
        return c

    def sr_p1(lis):
        li = []
        while True:
            sd = int(input("请输入位置索引："))
            if sd > (len(lis)-1) and sd != 20:
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
            print(li)
        return li

    def sr_p2(lis):
        li = []
        while True:
            sd = int(input("请输入位置索引："))
            if sd > (len(lis)-1) and sd != 20:
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
            print(li)
        return li

    def sr_p3(lis):
        li = []
        while True:
            sd = int(input("请输入位置索引："))
            if sd > (len(lis)-1) and sd != 20:
                continue
            if sd == 20:  # 20为提交指令
                break
            li.append(sd)
            print(li)
        return li
