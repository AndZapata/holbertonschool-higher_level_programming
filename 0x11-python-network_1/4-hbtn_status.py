#!/usr/bin/python3
''' Comment: fetches https://intranet.hbtn.io/status '''
if __name__ == "__main__":
    from urllib.request import urlopen
    with urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(str(html))))
        print('\t- content: {}'.format(html.decode('utf-8')))
