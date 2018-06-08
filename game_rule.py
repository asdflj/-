class Rule(object):
    def dibanchu(lis):
        lis_diban=[]
        for x in lis:
            a=(x-1) // 4 + 1
            lis_diban.append(a)
        return lis_diban
    def many_first(lis):#出牌排序，待用不操作
        count1 = []
        count2 = []
        count3 = []
        count4 = []
        for x in lis:
            if lis.count(x)==4:
                count4.append(x)
            elif lis.count(x)==3:
                count3.append(x)
            elif lis.count(x)==2:
                count2.append(x)
            else:
                count1.append(x)
        count1 = sorted(count1, reverse=True)
        count2 = sorted(count2, reverse=True)
        count3 = sorted(count3, reverse=True)
        count4 = sorted(count4, reverse=True)
        zong = count4+count3+count2+count1
        return zong
    






    def fanhui_xulie(lis):#判断出牌是否符合规则，不符合返回，玩家不要返回空列表
        def leixing(lis):#牌形选择
            b = 0
            if lis!=[]:
                for x in lis:
                    a = lis.count(x)
                    if a > b:
                        b = a
            return b
        def feiji(lis):#飞机类型判断
            pt=[]     
            count1,count2,count3,count4 = much_first(lis)     
            p3,p2,p1 = len(count3),len(count2),len(count1)
            if count3[0]-count3[-1]+1==len(count3)//3:
                #fly不带
                if p2 == 0 and p1 == 0:
                    pt+=[1,3, 3, 1, p3//3]
                    return pt
                #fly带单
                elif p2 == 0 and p1 == p3//3:
                    s = count3+count1
                    pt+=[1,3, 3, 2, p3//3,s[0]]
                    return pt
                elif p2+p1 == p3//3:
                    s = count3+count2+count1
                    pt+=[1,3, 3, 2, p3//3,s[0]]
                    return pt
                #fly带双
                elif p1 == 0 and p2//2==p3//3:
                    s=count3+count2
                    pt+=[1,3, 3, 3, p3//3,s[0]]
                    return pt
            return pt
        def putong_panduan(lis):#牌型判断
            pt=[]
            b = leixing(lis)
            if b == 1:
                if len(lis) == 1:
                    pt+=[1 , 1 , 1, lis[0]]
                    return pt           
                elif len(lis) >= 5:
                    if lis[0]-lis[-1]+1 == len(lis)\
                    and lis[0] <= 12: 
                        pt+=[1,1, len(lis), lis[0]]
                        return pt #单顺
            elif b == 2:
                if len(lis) == 2:
                    pt+=[1,2, 2, lis[0]]
                    return pt#单对
                    #加连对判断
                elif len(lis) >= 6 and len(lis)%2==0\
                 and lis[0]-lis[-1]+1 == len(lis)//2:
                    pt+=[1,2, len(lis), lis[0]]
                    return pt#连对
            elif b == 3:
                if len(lis) == 3:
                    pt+=[1,3, 1, lis[0]]
                    return pt#三不带           
                elif len(lis) == 4:
                    pt+=[1,3, 2, 1, lis[0]]
                    return pt#三带一          
                elif len(lis) == 5:
                    pt+=[1,3, 2, 2, lis[0]]
                    return pt#三带二
                else:
                    return feiji(lis)
            elif b == 4:
                if len(lis) == 6:
                    pt+=[1,4, 1, lis[0]]
                    return pt
                elif len(lis) == 8:
                    pt+=[1,4, 2, lis[0]]
                    return pt
            else:
                return pt

        

        daxiao_list=[]
        if len(lis) == 0:
            daxiao_list.append(4)
            return daxiao_list
        if len(lis) == 2 and lis[0] == lis[1] == 14:
            daxiao_list.append(3)
            #王炸
            return daxiao_list
        elif len(lis) == 4 and leixing(lis) == 4:
            daxiao_list.append(2)
            daxiao_list.append(lis[0])
            return daxiao_list       
        else:
            pt=putong_panduan(lis)
            if pt!=[]:
                return pt
            else:
                pt.append(100)
                return pt 




























    def bidaxiao(up,down):
        if up==[]:
            up=down
        else:
            if down[0]>up[0]:
                up=down
            elif down[0]==up[0] and up[0]==2:
                if down[1]>up[1]:
                    up=down
                else:
                    print("???")
                    #从新出
            else:
                if (down[0:len(down)-1:1]==\
                            up[0:len(down)-1:1])\
                             and down[-1]>up[-1]:
                    up=down
                else:
                    print("???")
        return up,down
                    #从新出