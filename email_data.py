# 由各个值组成的邮件内容,返回email_title,email_content
"""申购邮件信息"""


def email_subscribe_text(now_subscribe_data):
    """
    合成申购提醒邮件信息
    :param bond_data:
    :return:
    """
    global email_title, email_content
    email_title = ''
    email_content = ''
    for data in now_subscribe_data:
        email_title += data['SNAME'] + '\t'
        email_content += "债券简称：" + data['SNAME'] + "\n"
        email_content += "申购代码：" + data['CORRESCODE'] + "\n"
        email_content += "申购日期：" + data['STARTDATE'] + "\n"
        email_content += "正股价：" + str(data['ZGJ']) + "\n"
        email_content += "转股价：" + str(data['SWAPPRICE']) + "\n"
        email_content += "转股价值：" + str(data['ZGPRICE']) + "\n\n\n"

    email_title = "打新提醒：" + email_title

    return email_title, email_content


"""中签发布信息"""


def email_winning_rate_text(now_winning_data):
    """
    合成中签发布日邮件信息
    :param bond_data:
    :return:
    """
    global email_title, email_content
    email_title = ''
    email_content = ''
    # print(bond_winning_data)
    for data in now_winning_data:
        email_title += data['SNAME'] + '\t'
        email_content += "债券简称：" + data['SNAME'] + "\n"
        email_content += "中签号发布日：" + str(data['ZQHDATE']) + "\n"
        email_content += "中签率" + str(data['LUCKRATE']) + "\n\n\n"

    email_title = "中签发布日：" + email_title

    return email_title, email_content

