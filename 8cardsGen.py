# ! /usr/bin/dev python
# -*- coding: utf-8 -*-
# ########################################################
# 这个文件是从之前做好的6张牌里选出结尾3张并且与新增的5张形成一个8张组合，为整个16张牌序的第4张到第11张
# 这个8张组合必须满足以下条件：
# 1)第1张到第6张，形成一个6张组合
# 2)第2张到第7张，形成一个6张组合
# 3)第5张到第8张，形成一个4张组合
# 4)第3张到第8张，形成一个6张组合
# #########################################################
import pymysql
from baccarat import playerdrawcard
from baccarat import bdrawcard

def isCardsAvailable(cards):
    available = False
    cardslen = len(cards)
    if cardslen < 4 or cardslen > 6:
        return available

    playerHand = "{0}{1}".format(cards[0], cards[2])
    ppoint = int(playerHand[0]) + int(playerHand[1])
    if ppoint >= 10:
        ppoint = ppoint % 10

    bankerHand = "{0}{1}".format(cards[1], cards[3])
    bpoint = int(bankerHand[0]) + int(bankerHand[1])
    if bpoint >= 10:
        bpoint = bpoint % 10

    if cardslen == 4:
        if not playerdrawcard(ppoint, bpoint):
            if not bdrawcard(ppoint,bpoint, None, len(playerHand)):
                available = True

    else:
        if playerdrawcard(ppoint, bpoint):
            playerHand = "{0}{1}".format(playerHand, cards[4])
            ppoint = int(playerHand[0]) + int(playerHand[1]) + int(playerHand[2])
            if ppoint >= 10:
                ppoint = ppoint % 10
            if cardslen == 5:
                if not bdrawcard(ppoint, bpoint, None):
                    available = True
        else:
            if bdrawcard(ppoint, bpoint, cards[4], len(playerHand)):
                if cardslen == 6:
                    available = True
            elif not bdrawcard(ppoint, bpoint, cards[4], len(playerHand)):
                if cardslen == 5:
                    available = True

    return available




if __name__ == "__main__":
    db_name = "baccarat"
    table_name = "8cards"
    source1_name = "D:\\6cardsNOdraw.txt"  # 源数据文件1
    source2_name = "D:\\4cardsNOdraw.txt"  # 源数据文件2

    # 连接数据库
    try:
        connect = pymysql.Connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='wu221182',
            db='%s' % db_name,
            charset='utf8'
        )
        # 获取游标
        cursor = connect.cursor()
    except Exception as e:
        print(e)

    # 删除表格
    print("删除之前的表")
    sql_drop_table = "drop table %s" % table_name
    try:
        cursor.execute(sql_drop_table)
    except:
        print('删除表格 %s 失败' % table_name)


    # 创建表格
    print("创建新表格%s"%table_name)
    sql_create_table = f"create table {table_name} (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, "\
                       "preCards text, currentCards text)AUTO_INCREMENT=1 "
    print(sql_create_table)
    try:
        cursor.execute(sql_create_table)
    except:
        print('创建表格%s失败' % table_name)

    datasum = 0
    print("写入开始...")
    with open('%s' % source1_name, 'r') as sourcefile1:
        for line in sourcefile1:
            a = line.split(' ')
            #取出6张牌序列
            precards = a[4]
            #取出6张牌后3张
            firstpart = precards[3:6]

            for z in range(10):
                secondpart = '%s' % z
                #从4张牌文件里取出4张牌序列
                with open('%s' % source2_name, 'r') as sourcefile2:
                    for line1 in sourcefile2:
                        b = line1.split(' ')
                        temp1 = b[1]
                        temp2 = b[4]
                        thirdpart = temp1[0] + temp2[0] + temp1[1] + temp2[1]
                        #两个部分组合
                        cards = "{0}{1}{2}".format(firstpart, secondpart, thirdpart)

                        test1 = cards[0:6]
                        test2 = cards[1:7]
                        test3 = cards[2:8]
                        if isCardsAvailable(test3):
                            if isCardsAvailable(test2):
                                if isCardsAvailable(test1):
                                    # data = (None, precards, cards, playerhand, bankerhand, playerpoint, bankerpoint)
                                    sql_insert_data = "INSERT INTO %s (preCards,currentCards) VALUES ('%s', '%s') "%(table_name, precards, cards)
                                    cursor.execute(sql_insert_data)
                                    connect.commit()
                                    datasum = datasum + 1

    cursor.close()
    connect.close()
    print("写入结束。\n总共写入：", datasum, "条数据")



