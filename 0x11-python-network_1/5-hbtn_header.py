#!/usr/bin/python3
'''
Comment: takes a URL, sends a request and print a header value in X-Request-Id
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    html = requests.get(url)
    print('{}'.format(html.headers['X-Request-Id']))
