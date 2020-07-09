
"""获取数据"""
import json

import requests


def get_data(url):
    try:
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        response = requests.get(url, headers=header)
        status_code = response.status_code
        print("状态码：", status_code)
        response.encoding = response.apparent_encoding
        json_data = json.loads(response.text)

    except Exception as err:
        print(err)
        # get_data(url)
        return ''
    return json_data