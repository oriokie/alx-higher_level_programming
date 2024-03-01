#!/usr/bin/python3
"""
Module that takes in a URL and the displays the X-Request-Id variable found in
the header of the reposne
"""
from sys import argv
import requests


def main():
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))


if __name__ == '__main__':
    main()
