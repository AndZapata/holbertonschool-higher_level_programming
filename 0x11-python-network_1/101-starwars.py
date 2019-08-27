#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    from requests import get, post
    from sys import argv
    url = 'https://swapi.co/api/people'
    req = post(url, params={'search': argv[1]})
    in_file = req.json()
    counter = in_file.get('count')
    print("Number of results: {}".format(counter))
    for answer in in_file.get('results'):
        print(answer.get('name'))
    while in_file.get('next'):
        in_file = get(in_file.get('next')).json()
        for answer in in_file.get('results'):
            print(answer.get('name'))
