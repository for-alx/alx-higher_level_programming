#!/usr/bin/python3
"""
Response header value.
"""
if __name__ == '__main__':
    import sys
    import requests

    response = requests.get(str(sys.argv[1]))
    print(response.headers['X-Request-Id'])
