from game_liucheng import Liucheng as L

def main():
    paly1, paly2, paly3, dipai = L.fenpai()
    
    king_num,lis_123= L.jiaodizhu()
    
    paly1,paly2,paly3 = L.fendizhu\
        (paly1, paly2, paly3, dipai,king_num)
        #paly系列为原始列表
    win_num=L.game_time_start(play1,play2,play3,lis_123)

    L.end_result()

    print("Good Game!")



if __name__ == '__main__':
    main()