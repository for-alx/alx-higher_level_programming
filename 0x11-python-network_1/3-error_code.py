#!/usr/bin/python3
"""
Error code.
"""
if __name__ == '__main__':
    import sys
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError

    req = Request(str(sys.argv[1]))
    try:
        with urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
