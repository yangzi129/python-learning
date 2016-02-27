# -*- coding: utf-8 -*-

import mysql.connector

#从文件中读取信息
def file_read(filename):
	with open(filename,'r') as f:
		lines = f.readlines()
	for n in range(0,200):
		lines[n] = lines[n].strip()
	return lines

def mysql_write():
	lines = file_read("../0001/result.txt")
	conn = mysql_connector.connect(user = 'root', password = '12345', database = 'test', use_unicode = True)
	cursor = conn.cursor()
	cursor.execute("creat table promo_code (id int(3) primary key, number varchar(8))")
	for i in range(0, 200):
		cursor.execute('insert into promo_code (id, number) values (%s, %s)', [n+1, lines[n]])
	conn.commit()
	cursor.close()
	conn.close()
	print(finish)

if __name__ == '__main__':
	mysql_write()