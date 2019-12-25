# 通过hashlib库将密码hash后存入数据库
import mysqlx.connection
import time
import hashlib
import mysql.connector
print('begin'.center(30, '*'))
print('进行中，请稍等。。。。。。。。')
start = time.time()
conn = mysql.connector.connect(host='192.168.137.239', user='admin', password='123456', database='mysql')
cursor = conn.cursor()


def hash(pwd):
    method = hashlib.sha1()
    method.update(pwd.encode('utf-8', errors='ignore'))
    return method.hexdigest()


try:
    with open(r'C:\Users\11826\Desktop\18万条密码.txt', 'r', encoding='utf-8', errors='ignore') as file:
        for password in file:
            cursor.execute('insert into society.18wangcode_sha1_hash (pwd, hash_values) values (%s, %s)',
                           (password, hash(password)))
except:
    print('error')
finally:
    cursor.close()
    conn.commit()
    conn.close()
end = time.time()
print('结束，共耗时：{:.2f}秒'.format(end-start))
