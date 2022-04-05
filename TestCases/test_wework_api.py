# -*- coding: utf-8 -*-
# @Time : 2022/3/15 0:28 
# @Author : ZhangChao  
# @File : test_wework_api.py   
# @Project : apitest
import allure
from apitest.Api.address_book.department_api import DepartmentApi


@allure.feature("测试模块：通讯录部门")
class TestDepartment():
    def setup_class(self):
        self.department = DepartmentApi()
        self.department.get_token()

    @allure.title("测试标题：获取部门列表")
    @allure.story("测试名称：获取部门列表")
    @allure.severity(allure.severity_level.MINOR)
    def test_department_list(self):
        with allure.step("步骤1、获取部门列表"):
            result = self.department.department_list()
        assert result.status_code == 200

    @allure.title("测试标题：创建部门")
    @allure.story("测试名称：创建部门")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_department_create(self):
        result = self.department.department_create(name="宋国", parentid=1, id=10006)
        assert result.status_code == 200

    @allure.title("测试标题：删除部门")
    @allure.story("测试名称：删除部门")
    @allure.severity(allure.severity_level.NORMAL)
    def test_department_delete(self):
        result = self.department.department_delete(id=10006)
        assert result.status_code == 200
