#!/usr/bin/python3
"""
Response header value.
"""
if __name__ == '__main__':
    import sys
    from urllib.request import Request, urlopen
    req = Request(str(sys.argv[0]))
    with urlopen(req) as response:
        the_page = response.read()
        print(response.info().get('X-Request-Id'))
