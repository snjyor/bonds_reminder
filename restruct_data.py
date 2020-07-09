
"""获取申购信息"""


def get_subscribe_text(subscribe_json_data):
    """
    从json_data中提取申购数据
    :param html:
    :return:
    """
    bond_subscribe_data = []
    for data in subscribe_json_data:
        dict = {}
        try:
            dict['STARTDATE'] = data['STARTDATE']  # 申购日期
            dict['BONDCODE'] = data['BONDCODE']  # 债券代码
            dict['SNAME'] = data['SNAME']  # 债券简称
            dict['CORRESCODE'] = data['CORRESCODE']  # 申购代码
            dict['ZGJ'] = data['ZGJ']  # 正股价
            dict['SWAPPRICE'] = data['SWAPPRICE']  # 转股价
            dict['ZGPRICE'] = (100 * float(dict['ZGJ'])) / float(dict['SWAPPRICE'])  # 转股价值
            # 债现价
            # 转股溢价率
            bond_subscribe_data.append(dict)
        except Exception as err:
            print(err)
    return bond_subscribe_data


"""获取中签信息"""


def get_winning_rate_text(winning_json_data):
    """
    从json_data中提取中签数据
    :param html:
    :return:
    """
    bond_winning_data = []
    for data in winning_json_data:
        dict = {}
        try:
            dict['SNAME'] = data['SNAME']  # 债券简称
            dict['CORRESCODE'] = data['CORRESCODE']  # 申购代码
            dict['ZQHDATE'] = data['ZQHDATE']  # 中签号发布日
            dict['LUCKRATE'] = data['LUCKRATE']  # 中签率
            bond_winning_data.append(dict)
        except Exception as err:
            print(err)
    return bond_winning_data

