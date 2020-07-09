from datetime import datetime

def filter_subscribe_data(json_data):
    """
    筛选出申购日期大于今天的数据
    :param json_data:
    :return:
    """
    subscribe_json_data = []
    for data in json_data:
        STARTDATE = data['STARTDATE'].split('T')[0]  # 申购日期 <class 'str'> 2020-07-06T00:00:00
        # STARTDATE = '2020-07-07'
        STARTDATE = datetime.strptime(STARTDATE, '%Y-%m-%d').date()  # 把获取的时间转换成<class 'datetime.datetime'>格式
        now_date = datetime.now().date()
        if STARTDATE < now_date:
            # print("可转债信息过期！")
            continue
        subscribe_json_data.append(data)
    return subscribe_json_data


def filter_winning_data(json_data):
    """
    从总数据json_data中筛选出中签发布日数据
    :param json_data:
    :return:
    """
    winning_json_data = []
    for data in json_data:
        ZQHDATE = data['ZQHDATE'].split('T')[0]  # 申购日期 <class 'str'> 2020-07-06T00:00:00
        # STARTDATE = '2020-07-07'
        ZQHDATE = datetime.strptime(ZQHDATE, '%Y-%m-%d').date()  # 把获取的时间转换成<class 'datetime.datetime'>格式
        now_date = datetime.now().date()
        if ZQHDATE < now_date:
            continue
        winning_json_data.append(data)
    return winning_json_data

