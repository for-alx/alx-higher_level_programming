#!/usr/bin/python3
"""
POST an email.
"""

if __name__ == '__main__':
    import sys
    from urllib.request import Request, urlopen
    import urllib.parse

    value = {'email': str(sys.argv[2])}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(str(sys.argv[1]), data)
    with urlopen(req) as response:
        the_page = response.read()
        print(str(the_page.decode('utf-8')))
