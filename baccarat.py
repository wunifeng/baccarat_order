def playerdrawcard(ppoint, bpoint, pcardsnum=2):
    if pcardsnum > 2:
        return False

    if ppoint < 6 and bpoint <= 7:
        return True

    return False

def bdrawcard(ppoint, bpoint, pthirdcard, pcardsnum = 3, bcardnum=2):
    if bcardnum > 2:
        return False
    if pcardsnum == 3:
        if bpoint >= 7:
            return False
        if bpoint == 6:
            if pthirdcard == 6 or pthirdcard ==7:
                return True
            else:
                return False
        if bpoint == 5:
            if pthirdcard == 0 or pthirdcard ==1 or pthirdcard == 2 or pthirdcard == 3 or pthirdcard ==8 or pthirdcard == 9:
                return False
            else:
                return True
        if bpoint == 4:
            if pthirdcard == 0 or pthirdcard == 1 or pthirdcard == 8 or pthirdcard == 9:
                return False
            else:
                return True
        if bpoint == 3:
            if pthirdcard == 8:
                return False
            else:
                return True
        if bpoint < 3:
            return True
    elif pcardsnum ==2:
        if ppoint >= 8:
            return False
        if bpoint <= 5:
            return True
    else:
        return False

    return False


if __name__ == "__main__":
    n = 10000
    c = ''
    with open('D:\\4cardsNOdraw.txt', 'w') as f:
        f.writelines(c)
    while n < 20000:
        p = ''
        b = ''
        # convert n to str
        temp = '%d' % n
        totalCards = len(temp) - 1
        playerHand = [None, None]
        bankerHand = [None, None]

        playerHand[0] = temp[1]
        playerHand[1] = temp[3]
        ppoint = int(playerHand[0]) + int(playerHand[1])
        if ppoint >= 10:
            ppoint = ppoint % 10

        bankerHand[0] = temp[2]
        bankerHand[1] = temp[4]
        bpoint = int(bankerHand[0]) + int(bankerHand[1])
        if bpoint >= 10:
            bpoint = bpoint % 10

        if totalCards == 6:
            playerHand.append(temp[5])
            bankerHand.append(temp[6])

        if totalCards == 5:
            playerHand.append(temp[5])

        if not playerdrawcard(ppoint,bpoint):
            p = 'p no draw'
            if not bdrawcard(ppoint,bpoint,None,2):
                b = 'b no draw'
                content = 'pcards: ' + "".join(playerHand) + '  ' + 'bcards: ' + "".join(
                    bankerHand) + '  ' + 'ppoint: ' + str(ppoint) + '  ' + 'bpoint: ' + str(
                    bpoint) + '  ' + p + '  ' + b + '\n'
                c = "".join(content)
                with open('D:\\4cardsNOdraw.txt', 'a') as f:
                    f.writelines(c)

        n = n + 1





