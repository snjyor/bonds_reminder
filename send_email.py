from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
"""发送提醒邮件"""


def send_email(email_title='', email_content=''):
    """
    发送邮件
    :param email_title:
    :param email_content:
    :return:
    """
    pwd = 'zklrrgy****kbeeb'                # pwd、qq和sender修改为你自己的配置信息，你需要进到邮箱里配置好smtp，具体配置方法可百度

    qq = 'your_qq_number'
    sender = 'your_qq_email_address'
    receiver = ['your_email_address', ]     # 修改此处，将your_email_address改为你的邮箱地址

    host = 'smtp.qq.com'

    smtp = SMTP_SSL(host)
    smtp.ehlo(host)
    smtp.login(qq, pwd)

    msg = MIMEText(email_content, 'plain', 'utf-8')
    msg['subject'] = Header(email_title, 'utf-8')
    msg['from'] = 'bonds_reminder'
    msg['to'] = 'richer'

    smtp.send_message(msg, sender, receiver)
    print('成功发送邮件！')
    smtp.quit()

