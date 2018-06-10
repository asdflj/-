from game_liucheng import Liucheng as L
from game_tool import Tool as T


def main():
    play1, play2, play3, dipai = L.fenpai()

    king_num, lis_123 = L.jiaodizhu()

    play1, play2, play3 = L.fendizhu(play1, play2, play3, dipai, king_num)
    # play系列为原始列表
    win_num = L.game_time_start(play1, play2, play3, lis_123)

    L.end_result(king_num, win_num)

    print("Good Game!")


if __name__ == '__main__':
    main()
