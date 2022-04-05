# -*- coding: utf-8 -*-
# @Time : 2022/3/19 18:34 
# @Author : ZhangChao  
# @File : base_api.py   
# @Project : apitest
import json
import requests


class BaseApi():
    def request(self, request:dict):
        if "url" in request:
            return self.http_request(request)

    def http_request(self, request):
        r = requests.request(**request)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r



