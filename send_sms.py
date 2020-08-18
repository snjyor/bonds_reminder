from twilio.rest import TwilioRestClient


def subscribe_message_data(now_subscribe_data):
    """
    合成申购提醒短信信息
    :param bond_data:
    :return:
    """
    global subscribe_message_content
    subscribe_message_title = "打新债提醒！！快登录账号打新！\n"
    subscribe_message_content = ""
    # for data in now_subscribe_data:
    #     subscribe_message_content += "债券简称：" + data['SNAME'] + "\n"
    #     subscribe_message_content += "申购代码：" + data['CORRESCODE'] + "\n"
    #     subscribe_message_content += "申购日期：" + data['STARTDATE'] + "\n"
    #     subscribe_message_content += "正股价：" + str(data['ZGJ']) + "\n"
    #     subscribe_message_content += "转股价：" + str(data['SWAPPRICE']) + "\n"
    #     subscribe_message_content += "转股价值：" + str(data['ZGPRICE']) + "\n\n\n"

    subscribe_message_content = subscribe_message_title + subscribe_message_content

    return subscribe_message_content


def winning_message_data(now_winning_data):
    """
        合成中签发布日短信信息
        :param bond_data:
        :return:
        """
    global winning_message_content
    winning_message_title = "中签日提醒！！快登录账号看看自己有没有中签吧！\n"
    winning_message_content = ""
    # for data in now_winning_data:
    #     winning_message_content += "债券简称：" + data['SNAME'] + "\n"
    #     winning_message_content += "中签号发布日：" + str(data['ZQHDATE']) + "\n"
    #     winning_message_content += "中签率" + str(data['LUCKRATE']) + "\n\n\n"

    winning_message_content = winning_message_title + winning_message_content

    return winning_message_content


def send_subscribe_message(subscribe_message_content):
    # Your Account SID from twilio.com/console
    account_sid = "ACf0da731e19503885d1484b0532ceb9**" # 你自己的account_sid
    # Your Auth Token from twilio.com/console
    auth_token = "d83bfaefbb55608a20d95931299dec**" # 你自己的auth_token

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        to="+86153****2026",# 你的手机号码，需要加上+86，如：+8615322223333
        from_="+125****1012",# twilio服务端获取到的号码
        body=subscribe_message_content)# 短信内容

    message_sid = message.sid

    return message_sid


def send_winning_message(winning_message_content):
    # Your Account SID from twilio.com/console
    account_sid = "ACf0da731e19503885d1484b0532ceb9**"   # 你自己的account_sid
    # Your Auth Token from twilio.com/console  
    auth_token = "d83bfaefbb55608a20d95931299dec**"  # 你自己的auth_token

    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        to="+86153****2026",   # 你的手机号码，需要加上+86，如：+8615322223333
        from_="+125****1012",  # twilio服务端获取到的号码
        body=winning_message_content)  # 短信内容
    message_sid = message.sid

    return message_sid

if __name__ == '__main__':
    winning_message_content = "测试短信内容"
    message_sid = send_winning_message(winning_message_content)
    print(message_sid)
