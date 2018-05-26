import random


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


def paixu(list_need):
    list_fin = sorted(list_need, reverse=True)
    return list_fin


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

# 将发牌导出到列表
paly1, paly2, paly3, dipai = fapai()
paly1_fh = paixu(paly1)
paly2_fh = paixu(paly2)
paly3_fh = paixu(paly3)
dipai_fh = paixu(dipai)

# # 将发牌排序完成的列表翻译 并发送给客户端
# print('paly1_fh', fanyi(paly1_fh))
# print('paly2_fh', fanyi(paly2_fh))
# print('paly3_fh', fanyi(paly3_fh))
# print('dipai_fh', fanyi(dipai_fh))

# # 进入分地主阶段,且把结果发送给客户端

# caozuo1,caozuo2,caozuo3 = fendizhu()
# caozuo1 = sorted(caozuo1, reverse=True)
# caozuo2 = sorted(caozuo2, reverse=True)
# caozuo3 = sorted(caozuo3, reverse=True)

# def fendizhu():
#     three = int(input('请输入地主为（1or2or3）：'))
#     if three == 1:
#         dizhu1 = dipai+paly1
#         caozuo1 = dizhu1
#         caozuo2 = paly2
#         caozuo3 = paly3
#         print("地主为1")
#         print('1:', fanyi(paixu(dizhu1)))
#         print('2:', fanyi(paly2_fh))
#         print('3:', fanyi(paly3_fh))
#     elif three == 2:
#         dizhu2 = dipai+paly2
#         caozuo1 = paly1
#         caozuo2 = dizhu2
#         caozuo3 = paly3
#         print("地主为2")
#         print('1:', fanyi(paly1_fh))
#         print('2:', fanyi(paixu(dizhu2)))
#         print('3:', fanyi(paly3_fh))
#     elif three == 3:
#         dizhu3 = dipai+paly3
#         caozuo1 = paly1
#         caozuo2 = paly2
#         caozuo3 = dizhu3
#         print("地主为3")
#         print('1:', fanyi(paly1_fh))
#         print('2:', fanyi(paly2_fh))
#         print('3:', fanyi(paixu(dizhu3)))
#     else:
#         print('wrong num')
#     return caozuo1,caozuo2,caozuo3





# #出牌阶段
# while True:
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#     for x in range(3):
#         if x == 0:
#             print('play1:', fanyi(paixu(caozuo1)))
#         elif x == 1:
#             print('play2:', fanyi(paixu(caozuo2)))
#         elif x == 2:
#             print('play3:', fanyi(paixu(caozuo3)))
#         print('请%d出牌' % (x+1))

#         out_list = []
#         while True:
#             y = int(input('请输入位置索引'))
#             if y == 20:
#                 break
#             out_list.append(y)
#         out_list = paixu(out_list)

#         if x == 0:
#             qqq = []
#             for q in out_list:
#                 qq = fanyi([caozuo1[q]])
#                 qqq += qq
#                 del caozuo1[q]
#             print('play1出的牌为', qqq)
#         if x == 1:
#             qqq = []
#             for q in out_list:
#                 qq = fanyi([caozuo2[q]])
#                 qqq += qq
#                 del caozuo2[q]
#             print('play2出的牌为', qqq)
#         if x == 2:
#             qqq = []
#             for q in out_list:
#                 qq = fanyi([caozuo3[q]])
#                 qqq += qq
#                 del caozuo3[q]
#             print('play3出的牌为', qqq)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
