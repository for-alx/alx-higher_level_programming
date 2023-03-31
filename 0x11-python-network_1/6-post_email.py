#!/usr/bin/python3
"""
POST an email.
"""
if __name__ == '__main__':
    import sys
    import requests

    value = {'email': str(sys.argv[2])}
    response = requests.post(str(sys.argv[1]), data=value)
    print(response.content.decode('utf-8'))
