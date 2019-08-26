#!/usr/bin/python3
'''
comment: takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
'''
if __name__ == "__main__":
    import requests
    from sys import argv
    q = ""
    if len(argv) > 1:
        q = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    value = {'q': q}
    req = requests.post(url, value)
    try:
        in_file = req.json()
    except:
        print("Not a valid JSON")
    else:
        if in_file:
            print("[{}] {}".format(in_file.get('id'), in_file.get('name')))
        else:
            print("No result")
