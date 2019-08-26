#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    user = argv[1]
    passwd = argv[2]
    req = requests.get(url, auth=(user, passwd))
    in_file = req.json()
    print("{}".format(in_file.get('id')))
