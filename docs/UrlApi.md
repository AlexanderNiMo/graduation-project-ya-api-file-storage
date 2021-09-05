# file_storage_api.UrlApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_task_api_v1_download_file_post**](UrlApi.md#download_task_api_v1_download_file_post) | **POST** /api/v1/download_file | Добавление информации о местонахождении файла
[**get_streaming_url_api_v1_streaming_url_get**](UrlApi.md#get_streaming_url_api_v1_streaming_url_get) | **GET** /api/v1/streaming_url | Добавление информации о местонахождении файла
[**upload_task_api_v1_upload_file_post**](UrlApi.md#upload_task_api_v1_upload_file_post) | **POST** /api/v1/upload_file | Добавление информации о местонахождении файла

# **download_task_api_v1_download_file_post**
> Object download_task_api_v1_download_file_post(file_id)

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
api_instance = file_storage_api.UrlApi()
file_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.download_task_api_v1_download_file_post(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->download_task_api_v1_download_file_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**str**](.md)|  | 

### Return type

[**Object**](Object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = file_storage_api.UrlApi()
body = file_storage_api.FileLocation() # FileLocation | 
cdn = file_storage_api.CDN() # CDN | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.get_streaming_url_api_v1_streaming_url_get(body, cdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->get_streaming_url_api_v1_streaming_url_get: %s\n" % e)
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

# **upload_task_api_v1_upload_file_post**
> Object upload_task_api_v1_upload_file_post(body, cdn)

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
api_instance = file_storage_api.UrlApi()
body = file_storage_api.FileLocation() # FileLocation | 
cdn = file_storage_api.CDN() # CDN | 

try:
    # Добавление информации о местонахождении файла
    api_response = api_instance.upload_task_api_v1_upload_file_post(body, cdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UrlApi->upload_task_api_v1_upload_file_post: %s\n" % e)
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

