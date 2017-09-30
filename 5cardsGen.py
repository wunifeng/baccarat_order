from baccarat import playerdrawcard
from baccarat import bdrawcard

if __name__ == "__main__":

    # 清空文件"D:\\5cardsNOdraw.txt"
    c = ''
    with open('D:\\5cardsNOdraw.txt', 'w') as f5:
        f5.writelines(c)

    # 打开文件
    with open('D:\\4cardsNOdraw.txt', 'r') as f4:
        print("文件名为: ", f4.name)
        for line in f4:
            print("读取的数据为: %s" % (line))

            a = line.split(' ')
            phand = a[1]
            bhand = a[4]
            ppoint = int(a[7])
            bpoint = int(a[10])

            for i in range(10):
                '''
                把新加入的牌加到队列最前端 
                '''
                tcards = phand[0] + bhand[0] + phand[1] + bhand[1]
                content = "四张牌为： " + "".join(tcards) + "  "

                tcards = '%d' % i + tcards
                content = content + "五张牌为： " + "".join(tcards) + "  "
                if tcards == ['8','0','0','0','8']:
                    pass

                print(content)

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

                if playerdrawcard(ppoint, bpoint):
                    playerHand.append(tcards[4])
                    ppoint = int(playerHand[0]) + int(playerHand[1]) + int(playerHand[2])
                    if ppoint >= 10:
                        ppoint = ppoint % 10
                    if not bdrawcard(ppoint,bpoint,int(playerHand[2]),len(playerHand)):
                        content = content + "五张牌时，闲的牌是： " + "".join(playerHand) + "  庄家的牌是： " + "".join(bankerHand) + " 闲家的点数是： " + str(ppoint) + " 庄家的点数是： " + str(bpoint) + "  \n"
                        with open("D:\\5cardsNOdraw.txt", 'a') as f5:
                            f5.writelines(content)

                else:
                    if bdrawcard(ppoint, bpoint, None, len(playerHand)):
                        bankerHand.append(tcards[4])
                        bpoint = int(bankerHand[0]) + int(bankerHand[1]) + int(bankerHand[2])
                        if bpoint >= 10:
                            bpoint = bpoint % 10
                        content = content + "五张牌时，闲的牌是： " + "".join(playerHand) + "  庄家的牌是： " + "".join(
                            bankerHand) + " 闲家的点数是： " + str(ppoint) + " 庄家的点数是： " + str(bpoint) + "  \n"
                        with open("D:\\5cardsNOdraw.txt", 'a') as f5:
                            f5.writelines(content)

