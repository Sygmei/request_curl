# Request Curl

A user-friendly wrapper for pycurl that simplifies HTTP requests.

## Installation
Use the package manager 
[pip](https://pip.pypa.io/en/stable/) 
to install [curlquest](https://pypi.org/project/request-curl/).

> NOTE: You need Python and libcurl installed on your system to use or build pycurl. Some RPM distributions of curl/libcurl do not include everything necessary to build pycurl, in which case you need to install the developer specific RPM which is usually called curl-dev.


```
pip install curlquest
```

# Quickstart
A curlquest session manages cookies, connection pooling, and configurations.

Basic Usage:
```python
import curlquest
s = curlquest.Session()
s.get('https://httpbin.org/get') # returns <Response [200]>
s.request('GET', 'https://httpbin.org/get') # returns <Response [200]>
```

Using a Context Manager
```python
import curlquest
with curlquest.Session() as session:
    session.get('https://httpbin.org/get') # returns <Response [200]>
```

# Features

## Response Object

The response object is similar to that of the [requests](https://pypi.org/project/requests/) library.

```python
import curlquest
s = curlquest.Session()
r = s.get("https://httpbin.org/get")

print(r) # prints response object
print(r.status_code) # prints status code
print(r.content) # prints response content in bytes
print(r.text) # prints response content as text
print(r.json) # prints response content as JSON
print(r.url) # prints response URL
print(r.headers) # prints response headers
```

## Proxy Support
Format the proxy as a string.

```python
import curlquest
s = curlquest.Session()
# supports authentication: r = s.get("https://httpbin.org/get", proxies="ip:port:user:password")
r = s.get("https://httpbin.org/get", proxies="ip:port")
```

## HTTP2
HTTP2 is disabled by default.

```python
import curlquest
s = curlquest.Session(http2=True)
r = s.get("https://httpbin.org/get")
```

## Cipher Suites
You can specify custom cipher suites as an array.

```python
import curlquest

cipher_suite = [
    "AES128-SHA256",
    "AES256-SHA256",
    "AES128-GCM-SHA256",
    "AES256-GCM-SHA384"
]
s = curlquest.Session(cipher_suite=cipher_suite)
r = s.get("https://httpbin.org/get")
```

## Debug Request
Set debug to True to print raw input and output headers.

```python
import curlquest
s = curlquest.Session()
r = s.get("https://httpbin.org/get", debug=True)
```

## Custom Headers
Specify custom headers as a dictionary.

```python
import curlquest
s = curlquest.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
r = s.get("https://httpbin.org/get", headers=headers)
```

## Data

```python
import curlquest
s = curlquest.Session()

# sending form data
form_data = {"key": "value"}
response = s.post("https://httpbin.org/post", data=form_data)

# sending json data
json_data = {"key": "value"}
response = s.post("https://httpbin.org/post", json=json_data)
```

# Usage with Curl-Impersonate
To use curlquest with [curl-impersonate](https://github.com/lwthiker/curl-impersonate), 
opt for our [custom Docker image](https://hub.docker.com/r/h3adex/request-curl-impersonate) by either pulling or building it. 
The image comes with curlquest and curl-impersonate pre-installed. 
Check below for a demonstration on impersonating firefox98 tls-fingerprint and curlquest with our custom Docker Image.

**Note**: This feature is still considered experimental. Only tested with firefox fingerprint

To pull the Docker image:

```bash
docker pull h3adex/request-curl-impersonate:latest
docker run --rm -it h3adex/request-curl-impersonate
```

Example Python code for a target website:

```python
import curlquest
from curlquest import FIREFOX98_CIPHER_SUITE, FIREFOX98_HEADERS

# impersonates ff98
session = curlquest.Session(
    http2=True, 
    cipher_suite=FIREFOX98_CIPHER_SUITE, 
    headers=FIREFOX98_HEADERS
)
response = session.get("https://tls.browserleaks.com/json")
# <Response [200]>
# "ja3_hash":"25e9b0dd5b8e9330b206eae87e885e19"
# same result as: 
# docker run --rm lwthiker/curl-impersonate:0.5-ff curl_ff98 https://tls.browserleaks.com/json
```

# Contributing

We welcome contributions through pull requests. 
Before making major changes, please open an issue to discuss your intended changes.
Also, ensure to update relevant tests.

# License
Ennis Blank <Ennis.Blank@fau.de>, Mauritz Uphoff <Mauritz.Uphoff@hs-osnabrueck.de>

[MIT](LICENSE)