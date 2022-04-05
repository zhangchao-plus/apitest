# -*- coding: utf-8 -*-
# @Time : 2022/3/19 18:23 
# @Author : ZhangChao  
# @File : department_api.py
# @Project : apitest
from apitest.Api.common_api.wework_api import WeWorkApi


class DepartmentApi(WeWorkApi):
    """通讯录管理-部门管理模块接口"""

    def department_list(self):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params": {
                "access_token": self.get_token()
            }
        }
        return self.request(data)

    def department_create(self, name, parentid, id, name_en=None, order=1):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {
                "access_token": self.get_token()
            },
            "json": {
                "name": name,
                "name_en": name_en,
                "parentid": parentid,
                "order": order,
                "id": id
            }
        }
        return self.request(data)

    def department_delete(self, id):
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {
                "access_token": self.get_token(),
                "id": id
            }
        }
        return self.request(data)

    def department_clear(self):
        r = self.department_list()
        department_id_list = [department["id"] for department in r.json()["department"]]
        for id in department_id_list:
            if id != 1:
                self.department_delete(id)


# if __name__ == "__main__":
#     r = DepartmentApi().department_clear()



