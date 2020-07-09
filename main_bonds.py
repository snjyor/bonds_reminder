import schedule
import logging

from get_all_data import get_data
from reminder import subscribe_reminder, winning_reminder

"""主函数"""
def main():
    url = "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=KZZ_LB2.0&token=70f12f2f4f091e459a279469fe49eca5"  # 东方财富
    print(url)  
    json_data = get_data(url)
    subscribe_reminder(json_data)
    winning_reminder(json_data)
    print("*" * 40 + "\n\n\n")


if __name__ == '__main__':
    try:
        # main()
        schedule.every().day.at('09:30').do(main)  # 每天9:30执行一次
        print("开始执行……")
        while True:
            schedule.run_pending()
    except Exception as err:
        logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                            filename='bonds_error.log',
                            filemode='a',
                            format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                            )
