from today_data import today_subscribe_data, today_winning_data
from email_data import email_subscribe_text, email_winning_rate_text
from filter_data import filter_subscribe_data, filter_winning_data
from restruct_data import get_subscribe_text, get_winning_rate_text
from send_email import send_email
from send_sms import subscribe_message_data, winning_message_data, send_subscribe_message, send_winning_message
from datetime import datetime


def subscribe_reminder(json_data):
    subscribe_json_data = filter_subscribe_data(json_data)  # 筛选数据
    # print('筛选后的申购数据:\n',subscribe_json_data)
    bond_subscribe_data = get_subscribe_text(subscribe_json_data)  # 重组需要的今天往后的数据
    print('整理筛选后的申购数据:\n')
    for i in bond_subscribe_data:
        print(i)
    print('\n')

    now_subscribe_data = today_subscribe_data(bond_subscribe_data)
    print('今天的申购数据:\n')
    for i in now_subscribe_data:
        print(i)
    print('\n')

    print("当前时间为：\n", datetime.now(), '\n')
    if len(now_subscribe_data) > 0:
        # 发送邮件
        email_title, email_content = email_subscribe_text(now_subscribe_data)  #
        print("发送可转债打新提醒邮件……")
        send_email(email_title, email_content)

        # 发送短信
        subscribe_message_content = subscribe_message_data(now_subscribe_data)
        print("发送可转债打新提醒短信……\n")
        print("短信内容：\n" + subscribe_message_content)
        try:
            message_sid = send_subscribe_message(subscribe_message_content)
            print("成功发送打新提醒短信：" + message_sid + "\n")
        except Exception as err:
            email_title = '短信发送失败！'
            email_content = '短信发送失败！检查代码或短信次数是否有误！\n' + str(err)
            send_email(email_title=email_title, email_content=email_content)
    else:
        print("今天没有可转债打新\n\n\n\n")


def winning_reminder(json_data):
    winning_json_data = filter_winning_data(json_data)
    # print('筛选后的中签数据:\n',winning_json_data)
    bond_winning_data = get_winning_rate_text(winning_json_data)
    print("整理筛选后的中签数据:\n")
    for i in bond_winning_data:
        print(i)
    print('\n')

    now_winning_data = today_winning_data(bond_winning_data)
    print('今天的中签数据:\n')
    for i in now_winning_data:
        print(i)
    print('\n')

    print("当前时间为：\n", datetime.now(), '\n')

    if len(now_winning_data) > 0:
        # 发送邮件
        email_title, email_content = email_winning_rate_text(now_winning_data)
        print("发送中签日发布提醒邮件……")
        send_email(email_title, email_content)

        # 发送短信
        winning_message_content = winning_message_data(now_winning_data)
        print("发送中签日发布提醒短信……")
        print("短信内容：\n" + winning_message_content)
        try:
            message_sid = send_winning_message(winning_message_content)
            print("成功发送中签日短信：" + message_sid + "\n")
        except Exception as err:
            email_title = '短信发送失败！'
            email_content = '短信发送失败！检查代码或短信次数是否有误！\n' + str(err)
            send_email(email_title=email_title, email_content=email_content)

    else:
        print("今天没有可转债中签公布\n\n\n\n")
