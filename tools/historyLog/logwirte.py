import time


def history_write(content):
    '''
    将聊天历史记录保存
    :param content:
    :return:
    '''
    with open("His_" + time.strftime("%Y_%m_%d") + ".txt", 'a') as f1:
        f1.writelines("Time: " + content['Time'] + '\n')
        f1.writelines('Sender: ' + content['Sender'] + '\n')
        f1.writelines('Type : ' + content['Type'] + '\n')
        f1.writelines('Message : ' + content['Message'] + '\n')

    msg = '\n\nTime: ' + content['Time'] + '\nSender: ' + content['Sender'] + '\nType : ' + content[
        'Type'] + '\nMessage : ' + content['Message']+'\n----------------------------------\n'

    return msg
