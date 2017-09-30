from baccarat import playerdrawcard
from baccarat import bdrawcard

if __name__ == "__main__":
    # 清空文件"D:\\7cardsNOdraw.txt"
    c = ''
    with open('D:\\7cardsNOdraw.txt', 'w') as f7:
        f7.writelines(c)

    # 打开文件
    with open('D:\\6cardsNOdraw.txt', 'r') as f6:
        print("读取文件名为: ", f6.name)

        for line in f6:
            a = line.split(' ')
            cards6 = a[4]
            phand = a[7]
            bhand = a[10]
            ppoint = int(a[12])
            bpoint = int(a[14])

            for i in range(10):
                # 把新加入的牌加到队列最前端
                tcards = ""
                tcards = a[4]
                content = "原6张牌为： " + cards6 + "  "
                tcards = '%d' % i + cards6
                content = content + "7张牌为： " + "".join(tcards) + "  "

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
                    if bdrawcard(ppoint,bpoint,int(playerHand[2]),len(playerHand)):
                        bankerHand.append(tcards[5])
                        bpoint = int(bankerHand[0]) + int(bankerHand[1]) + int(bankerHand[2])
                        if bpoint >= 10:
                            bpoint = bpoint % 10
                        content = content + "7张牌时前6张，闲的牌是： " + "".join(playerHand) + "  庄家的牌是： " + "".join(bankerHand) + " 闲家的点数是： " + str(ppoint) + " 庄家的点数是： " + str(bpoint) + "  \n"
                        print(content)
                        with open("D:\\7cardsNOdraw.txt", 'a') as f7:
                            f7.writelines(content)