#!/usr/bin/python3
''' handle the error code '''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    bad_req = requests.get(url)
    try:
        bad_req.raise_for_status()
    except:
        print('Error code: {}'.format(bad_req.status_code))
    else:
        print(bad_req.text)
