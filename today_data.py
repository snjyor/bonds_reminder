from datetime import datetime

def today_subscribe_data(bond_subscribe_data):
    now_subscribe_data = []
    for data in bond_subscribe_data:
        STARTDATE = data['STARTDATE'].split('T')[0]  # 申购日期 <class 'str'> 2020-07-06T00:00:00
        # STARTDATE = '2020-07-07'  # 测试日期
        STARTDATE = datetime.strptime(STARTDATE, '%Y-%m-%d').date()  # 把获取的时间转换成<class 'datetime.datetime'>格式
        now_date = datetime.now().date()
        if STARTDATE != now_date:
            continue
            # print(data['SNAME']+"的打新时间为："+STARTDATE)
        now_subscribe_data.append(data)
    # print("now_subscribe_data:", now_subscribe_data)
    return now_subscribe_data

def today_winning_data(bond_winning_data):
    now_winning_data = []
    for data in bond_winning_data:
        ZQHDATE = data['ZQHDATE'].split('T')[0]  # 申购日期 <class 'str'> 2020-07-06T00:00:00
        # ZQHDATE = '2020-07-07'  # 测试日期
        ZQHDATE = datetime.strptime(ZQHDATE, '%Y-%m-%d').date()  # 把获取的时间转换成<class 'datetime.datetime'>格式
        now_date = datetime.now().date()
        if ZQHDATE != now_date:
            continue
        now_winning_data.append(data)
    # print("now_winning_data:", now_winning_data)
    return now_winning_data
