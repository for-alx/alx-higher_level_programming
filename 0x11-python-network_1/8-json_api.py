#!/usr/bin/python3
"""
Search API
"""
if __name__ == '__main__':
    import sys
    import requests

    if len(sys.argv) == 1:
        data = None
    else:
        data = str(sys.argv[1])

    value = {'q': data}
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data=value)
        # print(response.content.decode('utf-8'))
        result = eval(response.content.decode('utf-8'))
        if len(result) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(result['id'], result['name']))
    except Exception:
        print('Not a valid JSON')
