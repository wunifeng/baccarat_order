# ! /usr/bin/python
# -*- coding: utf-8 -*-

#########################################################

# 这个文件是从之前做好的6张牌里选出头2张和结尾2张相同的序列

##########################################################

import pymysql

db_name = "baccarat"
table_name = "perfect6cards"
source_name = "D:\\6cardsNOdraw.txt"  # 源数据文件

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
sql_create_table = "create table %s (id int PRIMARY KEY NOT NULL AUTO_INCREMENT, preCards text, currentCards text, playerHand " \
                   "text, bankerHand text, currentPpoint int, currentBpoint int)AUTO_INCREMENT=1 " % table_name
print(sql_create_table)
try:
    cursor.execute(sql_create_table)
except:
    print('创建表格%s失败' % table_name)

datasum = 0
print("写入开始...")
with open('%s' % source_name, 'r') as sourcefile:
    for line in sourcefile:
        a = line.split(' ')
        cards = a[4]
        if (cards[0] == cards[3]) and (cards[1] == cards[4]) and (cards[2] == cards[5]):
            playerhand = a[7]
            bankerhand = a[10]
            playerpoint = int(a[12])
            bankerpoint = int(a[14])
            precards = cards[1:6]
            # data = (None, precards, cards, playerhand, bankerhand, playerpoint, bankerpoint)
            sql_insert_data = "INSERT INTO %s (preCards,currentCards, playerHand, bankerHand, currentPpoint, currentBpoint) VALUES ('%s', '%s', '%s', '%s', %d, %d) "%(table_name, precards, cards, playerhand, bankerhand, playerpoint, bankerpoint)
            cursor.execute(sql_insert_data)
            connect.commit()
            datasum = datasum + 1

cursor.close()
connect.close()
print("写入结束。\n总共写入：", datasum, "条数据")