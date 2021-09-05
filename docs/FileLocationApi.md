# file_storage_api.FileLocationApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_streaming_url_api_v1_streaming_url_get**](FileLocationApi.md#get_streaming_url_api_v1_streaming_url_get) | **GET** /api/v1/streaming_url | Добавление информации о местонахождении файла

# **get_streaming_url_api_v1_streaming_url_get**
> Object get_streaming_url_api_v1_streaming_url_get(body, cdn)

Добавление информации о местонахождении файла

Добавление информации о местонахождении файла

### Example
```python
from __future__ import print_function
import time
import file_storage_api
from file_storage_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = file_storage_api.FileLocationApi()
body = file_storage_api.FileLocation() # FileLocation | 
cdn = file_storage_api.CDN() # CDN | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.get_streaming_url_api_v1_streaming_url_get(body, cdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileLocationApi->get_streaming_url_api_v1_streaming_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FileLocation**](FileLocation.md)|  | 
 **cdn** | [**CDN**](.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

