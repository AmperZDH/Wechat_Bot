import sqlite3
import time
import wxpy


class sqlite_op():
    def __init__(self,db_address):
        self.sql = sqlite3.connect(db_address)
        # self.sql = sqlite3.connect('/Users/amber.d/Documents/Pycharm/ChatBot_wx/wxcontacts/wxContacts.db')
        self.cur = self.sql.cursor()
        print('DataBase Connection ')

    '''
    
        当有新的好友添加后
        执行跟新数据库的操作
    
    '''

    def update_contacts(self, friends_list):
        self.sql.execute('delete from wxcontacts')
        self.sql.commit()

        for i in friends_list:

            i = str(i)
            line = i.replace('<Friend: ', '')
            line = line.replace('>', '')
            # print(line, '===', time.time())

            self.sql.execute('insert into wxcontacts(name,time) values (?,?)', (line, time.time()))
            self.sql.commit()
            # print('insert successful')

    '''
    
    核对某个用户时间
    
    '''

    def check_time(self, name):
        old_time = self.cur.execute('select time from wxcontacts where name =(?)', (name,))
        # print(old_time)
        check_time = None
        for i in old_time:
            check_time = str(i)
            check_time = check_time.replace(',)', '')
            check_time = check_time.replace('(', '')
        return check_time

    '''
        更新时间
    '''

    def update_time(self, name):
        self.cur.execute('update wxcontacts set time=? where name = ?', (time.time(), name))
        self.sql.commit()
        # print('update_time Successful!!')

    '''
    关闭数据库
    '''

    def sql_close(self):
        self.sql.close()


# sql = sqlite_op('../../wxcontacts/wxContacts.db')
# bot = wxpy.Bot(cache_path=True)
# # bot = Bot(cache_path=True,console_qr=True)
# my_friend = bot.friends()
# list=my_friend.copy()
# sql.update_contacts(list)
# a=sql.check_time('相宁')
# print(a)