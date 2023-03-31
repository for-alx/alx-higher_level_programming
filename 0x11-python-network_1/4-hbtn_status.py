#!/usr/bin/python3
"""
 What's my status?.
"""
if __name__ == '__main__':
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.content.decode('utf-8')))
