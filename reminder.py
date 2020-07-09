from today_data import today_subscribe_data,today_winning_data
from email_data import email_subscribe_text, email_winning_rate_text
from filter_data import filter_subscribe_data, filter_winning_data
from restruct_data import get_subscribe_text, get_winning_rate_text
from send_email import send_email
from datetime import datetime

def subscribe_reminder(json_data):
    subscribe_json_data = filter_subscribe_data(json_data)      # 筛选数据
    print('筛选后的申购数据:\n',subscribe_json_data)
    bond_subscribe_data = get_subscribe_text(subscribe_json_data)  # 重组需要的今天往后的数据
    print('整理筛选后的申购数据:\n', bond_subscribe_data)
    now_subscribe_data = today_subscribe_data(bond_subscribe_data)
    print('今天的申购数据:\n', now_subscribe_data)
    print("当前时间为：\n", datetime.now())
    if len(now_subscribe_data)>0:
        email_title, email_content = email_subscribe_text(now_subscribe_data)  #
        print("发送可转债打新提醒邮件……")
        send_email(email_title, email_content)
    else:
        print("今天没有可转债打新\n\n\n\n")


def winning_reminder(json_data):
    winning_json_data = filter_winning_data(json_data)
    print('筛选后的中签数据:\n',winning_json_data)
    bond_winning_data = get_winning_rate_text(winning_json_data)
    print("整理筛选后的中签数据:\n",bond_winning_data)
    now_winning_data = today_winning_data(bond_winning_data)
    print('今天的中签数据:\n', now_winning_data)
    print("当前时间为：\n", datetime.now())
    if len(now_winning_data)>0:
        email_title, email_content = email_winning_rate_text(now_winning_data)
        print("发送中签日发布提醒邮件……")
        send_email(email_title, email_content)
    else:
        print("今天没有可转债中签公布\n\n\n\n")

