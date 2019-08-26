#!/usr/bin/python3
'''
Comment: takes a URL, sends a request and print a header value in X-Request-Id
'''
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print('{}'.format(response.headers.get('X-Request-Id')))
