#!/usr/bin/python3
"""
Module that takes in a URL and the displays the X-Request-Id variable found in
the header of the reposne
"""
from sys import argv
from urllib.request import Request, urlopen


def main():
    r = Request(argv[1])
    with urlopen(r) as response:
        print(response.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
