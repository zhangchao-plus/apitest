# -*- coding: utf-8 -*-
# @Time : 2022/3/15 0:28 
# @Author : ZhangChao  
# @File : wework_api.py   
# @Project : apitest
from apitest.Utils.base_api import BaseApi


class WeWorkApi(BaseApi):
    def get_token(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww74ffb2817ac4143a",
                "corpsecret": "LDv0xTTDtyuVK3IvhDCNzqa9FSwVaHHzjsAnWdu2rn4"
            },
            "headers": {
                "User-Agent": "PostmanRuntime/7.29.0"
            },
            "verify": False
        }
        r = self.request(data)
        return r.json()["access_token"]


if __name__ == "__main__":
    WeWorkApi().get_token()


