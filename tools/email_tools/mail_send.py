import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


class mail():

    def __init__(self, sender_address, smtp_server, mail_pwd):
        self.sender_address = sender_address
        self.smtp_server = smtp_server
        self.mail_pwd = mail_pwd
        self.server = smtplib.SMTP_SSL(self.smtp_server, 465)  # 如果邮件无法发送,就修改此端口号
        # self.server = smtplib.SMTP(self.smtp_server, 25)
        self.server.login(self.sender_address, self.mail_pwd)
        print('Mail Online!')

    '''
    # receiver_address 发送地址
    # msg_subject 主题
    # mst_text 发送的内容
    '''

    def send_text(self, receiver_address, msg_subject, msg_text):
        content_text = MIMEText(msg_text, 'plain', 'utf-8')
        content_text['From'] = self.sender_address
        content_text['To'] = receiver_address
        content_text['Subject'] = msg_subject

        try:
            self.server.sendmail(from_addr=self.sender_address, to_addrs=receiver_address, msg=content_text.as_string())
        except:
            print('Error:', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ' Send Fail\n')

    def send_file(self, receiver_address, msg_subject, file_path):
        # message = MIMEMultipart()
        message = MIMEText(open(file_path, 'rb').read(), 'plain', 'utf-8')
        message['From'] = Header(self.sender_address, 'utf-8')
        message['To'] = Header(receiver_address, 'utf-8')
        message['Subject'] = Header(msg_subject, 'utf-8')

        # message=MIMEText(open(file_path,'rb').read(),'base64','utf-8')
        # message.attach(att1)
        self.server.sendmail(from_addr=self.sender_address, to_addrs=receiver_address, msg=message.as_string())
        # try:
        #     self.server.sendmail(from_addr=self.sender_address, to_addrs=receiver_address,msg=message.as_string())
        #     print("邮件发送成功")
        # except smtplib.SMTPException:
        #     print("Error: 无法发送邮件")

    def send_close(self):
        self.server.close()

# sender_address = 'amberzdh@163.com'
# # mail_pwd='gtfzkraqtekcieda'
# mail_pwd = 'Amber123zdh'
# mail_receiver = 'amberzdh@163.com'
# smtp_server = 'smtp.163.com'
# e = mail(sender_address=sender_address, smtp_server=smtp_server, mail_pwd=mail_pwd)
# e.send_text(receiver_address=mail_receiver,whos_msg='Amber',msg_text='Hhhhhhhhhhhh')
# e.send_close()
