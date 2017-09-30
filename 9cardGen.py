# ! /usr/bin/python
# -*- coding: utf-8 -*-

from baccarat import playerdrawcard
from baccarat import bdrawcard

if __name__ == "__main__":
    # 清空文件"D:\\9cardsNOdraw.txt"
    c = ''
    with open('D:\\9cardsNOdraw.txt', 'w') as f9:
        f9.writelines(c)

    # 打开文件
    with open('D:\\6cardsNOdraw.txt', 'r') as f6:
        print("读取文件名为: ", f6.name)
        for line in f6:
            # print("读取的数据为: %s" % (line))
            a = line.split(' ')
            cards6 = a[4]

            for i in range(10):
                for j in range(10):
                    for k in range(10):
                        # 把新加入的牌加到队列最前端
                        tcards = ""
                        tcards = cards6[0]
                        content = "6张牌为： " + "".join(cards6) + "  "
                        precards = '%d' % i + '%d' % j + '%d' % k
                        tcards = precards + tcards
                        content = content + "9张牌为： " + "".join(precards) + "".join(cards6) + "  "

                        playerHand = [None, None]
                        bankerHand = [None, None]

                        playerHand[0] = tcards[0]
                        playerHand[1] = tcards[2]
                        ppoint = int(playerHand[0]) + int(playerHand[1])
                        if ppoint >= 10:
                            ppoint = ppoint % 10

                        bankerHand[0] = tcards[1]
                        bankerHand[1] = tcards[3]
                        bpoint = int(bankerHand[0]) + int(bankerHand[1])
                        if bpoint >= 10:
                            bpoint = bpoint % 10

                        if not playerdrawcard(ppoint, bpoint):
                            if not bdrawcard(ppoint,bpoint,None):
                                content = content + "9张牌第一手，闲的牌是： " + "".join(playerHand) + "  庄家的牌是： " + "".join(bankerHand) + " 闲家的点数是： " + str(ppoint) + " 庄家的点数是： " + str(bpoint) + "  \n"
                                print(content)
                                with open("D:\\9cardsNOdraw.txt", 'a') as f9:
                                    f9.writelines(content)

