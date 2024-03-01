#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to solve this challenge.

The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
"""

from sys import argv
import requests


def main():
    """Main Function"""
    user, passwd = argv[1], argv[2]
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(user, passwd))
    print(r.json().get('id'))


if __name__ == '__main__':
    main()
