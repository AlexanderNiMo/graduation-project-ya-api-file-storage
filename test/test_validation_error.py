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
from file_storage_api.models.validation_error import ValidationError  # noqa: E501
from file_storage_api.rest import ApiException


class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidationError(self):
        """Test ValidationError"""
        # FIXME: construct object with mandatory attributes with example values
        # model = file_storage_api.models.validation_error.ValidationError()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
