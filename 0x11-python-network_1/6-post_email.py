#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    value = {'email': argv[2]}
    req = requests.post(url, value)
    print(req.text)
