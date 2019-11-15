import time
from setting import *
from wxpy import *
from tools.email_tools import mail_send
from tools.sql_tools import sqlite_op
from tools.historyLog.logwirte import history_write

# bot = Bot(cache_path=True)
bot = Bot(cache_path=True, console_qr=-2)
my_friend = bot.friends()
friends_list = my_friend.copy()

# 登陆更新数据库
dbsql = sqlite_op.sqlite_op(db_address='wxcontacts/wxContacts.db')
dbsql.update_contacts(friends_list)
dbsql.sql_close()

bot.file_helper.send('<Bot Online now>')
bot.file_helper.send(DOC)

MY_NAME = bot.self.name  # 获取自己的微信名

REPLY_TIME = 60.0  # 默认60秒内不自动回复
bot_server = True
bot_reply = '< 自动回复 >'
VIP_list = []

print(time.strftime("%H:%M:%S : "), 'Bot Start Successful')


@bot.register(chats=my_friend, except_self=False)
def auto_reply(msg):
    global bot_server, bot_reply, VIP_list, REPLY_TIME, str
    content = {'Time': time.strftime("%Y_%m_%d %H:%M"), 'Sender': msg.sender.name, 'Type': msg.type,
               'Message': (msg.text + '\n')}
    mail = mail_send.mail(sender_address=EMAIL_ADDRESS, smtp_server=EMAIL_STMP, mail_pwd=EMAIL_PASSWORD)
    print(time.strftime("%H:%M:%S : "), 'Mail Server Start ')
    sql = sqlite_op.sqlite_op(db_address='wxcontacts/wxContacts.db')

    '''由于python无switch-case语法，由下if elif 语句'''
    if msg.sender.name == MY_NAME:
        if msg.text == 'help':
            bot.file_helper.send(DOC)
            return '<void>'

        elif msg.text == 'status':
            if bot_server == True:
                bol = 'True'
            else:
                bol = 'False'
            # print('bol '+bol)
            # print(REPLY_TIME)
            # tm=str(REPLY_TIME)
            # print('tm ' + tm)
            stat = '<------Bot Status------>:\n' \
                   '开启状态:\n' \
                   + str(bot_server) \
                   + '\n\n自动回复语句:\n' \
                   + bot_reply \
                   + '\n\n回复间隔时间:\n' \
                   + str(REPLY_TIME) \
                   + '\n\nVIP列表:\n'
            for i in VIP_list:
                stat += i + '\n'

            bot.file_helper.send(stat)
            return '<void>'


        # 数据库列表的更新
        elif msg.text == 'updatelist':
            sql.update_contacts(friends_list)
            print(time.strftime("%H:%M:%S : "), 'Friendlist already updated~~')
            bot.file_helper.send('<DataBase update complete>')
            return '<void>'

        elif msg.text == 'botopen':
            bot_server = True
            mail.send_text(receiver_address=EMAIL_ADDRESS, msg_subject='Bot', msg_text='WechatBot已启动')
            mail.send_close()
            bot.file_helper.send('<Chatbot open complete>')
            return '<void>'

        elif msg.text == 'botclose':
            bot_server = False
            mail.send_text(receiver_address=EMAIL_ADDRESS, msg_subject='Bot', msg_text='WechatBot掉线啦！！')
            mail.send_close()
            bot.file_helper.send('<Chatbot close complete>')
            return '<void>'

        elif msg.text[0:9] == 'autoreply':
            bot_reply = msg.text[10:]
            bot.file_helper.send('<Setting Auto reply ' + bot_reply + ' complete>')
            return '<void>'

        elif msg.text[0:6] == 'addVIP':
            VIP_list.append(msg.text[7:])
            bot.file_helper.send('<Adding ' + msg.text[7:] + 'in VIP Okey>')
            return '<void>'

        elif msg.text[0:5] == 'rmVIP':
            try:
                VIP_list.remove(msg.text[6:])
                bot.file_helper.send('<Removing ' + msg.text[6:] + 'for VIP Okey>')
                return '<void>'
            except:
                bot.file_helper.send('<Removing ' + msg.text[6:] + ' Failed>')
                return '<void>'

        elif msg.text == 'VIP':
            strlist = 'VIP列表:\n'
            for i in VIP_list:
                strlist += i + '\n'
            bot.file_helper.send(strlist)
            return '<void>'

        elif msg.text[0:4] == 'time':
            try:
                print(msg.text[5:])
                REPLY_TIME = float(msg.text[5:])
                bot.file_helper.send('<回复间隔设置为 ' + str(REPLY_TIME) + 's>')
                return '<void>'
            except:
                bot.file_helper.send('<!时间设置error>')
                return '<void>'

    print(content, '\n')

    '''替换信息'''
    sender_name = str(msg.sender)
    sender_name = sender_name.replace('<Friend: ', '')
    sender_name = sender_name.replace('>', '')
    # print(sender_name)

    '''记录聊天信息'''
    history_write(content)

    '''紧急事件转接功能，识别特定字符串的信息，将信息传入邮箱'''
    if (str(msg.text).find('alling') >= 0) and (bot_server == True):
        mail.send_file(receiver_address=EMAIL_ADDRESS, msg_subject=(sender_name + ' Calling'),
                       file_path=("His_" + time.strftime("%Y_%m_%d") + ".txt"))
        mail.send_close()
        print(time.strftime("%H:%M:%S : "), 'Mail Server Close')
        return '<上述记录已发送Am邮箱>'

    '''特别关心消息转接'''
    if sender_name in VIP_list:
        print('VIP人员消息:')
        mail.send_text(receiver_address=EMAIL_ADDRESS, msg_subject=sender_name + ' -VIP-',
                       msg_text='message_type: ' + msg.type + '\nmessage_text: ' + msg.text)
        print('VIP消息已转接邮箱')
        mail.send_close()

    print('Time_split of ', sender_name, '== ', (float(time.time()) - float(sql.check_time(sender_name))))

    if ((float(sql.check_time(sender_name)) + float(REPLY_TIME)) <= float(time.time())) and (
            bot_server == True) and sender_name not in VIP_list:
        print(time.strftime("%H:%M:%S : "), sender_name, ' 已回复')
        sql.update_time(sender_name)

        if msg.type == TEXT:
            return bot_reply

        elif msg.type == MAP:
            return bot_reply

        elif msg.type == CARD:
            return bot_reply

        elif msg.type == SHARING:
            return bot_reply

        elif msg.type == PICTURE:
            return bot_reply

        elif msg.type == RECORDING:
            return bot_reply

        elif msg.type == ATTACHMENT:
            return bot_reply

        elif msg.type == VIDEO:
            return bot_reply

        else:
            return bot_reply


bot.join()
mail = mail_send.mail(sender_address=EMAIL_ADDRESS, smtp_server=EMAIL_STMP, mail_pwd=EMAIL_PASSWORD)
mail.send_text(receiver_address=RECEIVER_EMAIL, msg_subject='WARNING', msg_text='小安同志掉线了!!!!')
mail.send_close()
print('Logout Time: ', time.strftime("%H:%M:%S : "))
