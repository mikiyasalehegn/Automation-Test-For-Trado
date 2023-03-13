import json
import allure
import jsonpath
import requests

from Server.API.Constants.login import Login
from Server.API.Constants.sorting_constants import Sorting


class Test_Sorting(Login):
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Test api for sorting products from low price")
    def test_api_for_login(self):
        url = self.url
        data = self.body
        res = requests.post(url, json=data)
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 10
