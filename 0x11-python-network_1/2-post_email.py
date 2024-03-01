#!/usr/bin/python3
"""Python Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
from urllib import parse
from urllib.request import Request, urlopen
from sys import argv


def main():
    """Main Function"""
    url = argv[1]
    values = {'email': argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))


if __name__ == '__main__':
    main()
