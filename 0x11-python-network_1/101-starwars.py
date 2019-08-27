#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://swapi.co/api/people'
    req = requests.post(url, params={'search': argv[1]})
    in_file = req.json()
    counter = in_file.get('count')
    print("Number of results: {}".format(counter))
    for answer in in_file.get('results'):
        print(answer.get('name'))
