#!/usr/bin/python3
''' handle the error code '''
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv
    req = Request(argv[1])
    try:
        with urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
