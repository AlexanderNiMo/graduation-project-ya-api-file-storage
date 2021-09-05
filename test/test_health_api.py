# coding: utf-8

"""
    API для работы с файловыми ресурсами контента 

    Получение стриминг ссылок, загрузка данных в хранилище и отправка данных в облачные s3 хранилища  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import file_storage_api
from file_storage_api.api.health_api import HealthApi  # noqa: E501
from file_storage_api.rest import ApiException


class TestHealthApi(unittest.TestCase):
    """HealthApi unit test stubs"""

    def setUp(self):
        self.api = HealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check_api_health_check_get(self):
        """Test case for health_check_api_health_check_get

        Health Check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
