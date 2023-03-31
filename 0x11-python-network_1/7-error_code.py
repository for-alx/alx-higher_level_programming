#!/usr/bin/python3
"""
Error code.
"""
if __name__ == '__main__':
    import sys
    import requests

    response = requests.get(str(sys.argv[1]))
    if response.status_code > 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.content.decode('utf-8'))
