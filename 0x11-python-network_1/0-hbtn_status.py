#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    from urllib.request import Request, urlopen
    req = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(req) as response:
        the_page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(the_page)))
        print('\t- content: {}'.format(the_page))
        print('\t- utf8 content: {}'.format(the_page.decode('utf-8')))
