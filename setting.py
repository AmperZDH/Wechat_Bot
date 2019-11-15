'''
Global settings
'''
# 设置你的邮箱号
EMAIL_ADDRESS = 'amberzdh@163.com'

# STMP开启下的邮箱密码
EMAIL_PASSWORD = 'Amber123zdh'

# 邮箱的STMP地址
EMAIL_STMP = 'smtp.163.com'

# 收件人，建议填自己便于实现特别关心
RECEIVER_EMAIL = 'amberzdh@163.com'

# help功能文档
DOC = '【功能说明】\n向自己的账号发送关键词可使用功能，传输助手负责提示使用功能情况:\n\n' \
      'help:显示帮助文档\n' \
      'status:显示机器人状态\n' \
      'updatelist:更新数据库内好友列表\n' \
      'botopen:开启机器人\n' \
      'botclose:关闭机器人\n' \
      'VIP:查看所有设置的特别关心\n\n' \
      '下列为回复语句,特别关心设置:\n' \
      'addVIP@+所要设置特别关心的人\n' \
      'rmVIP@+所要取消特别关心的人\n' \
      'autoreply@+所要设置自动回复语句\n' \
      'time@+所要设置的回复时间间隔\n' \
      '例:addVIP@Amber\n'
