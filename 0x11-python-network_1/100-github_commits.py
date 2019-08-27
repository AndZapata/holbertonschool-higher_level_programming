#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    req = requests.get(url)
    in_file = req.json()
    for answer in in_file[:10]:
        print("{}".format(answer.get('sha')), end=': ')
        print("{}".format(answer.get('commit').get('author').get('name')))
