#!/usr/bin/python3
"""Module for fetching a url"""
from urllib.request import Request, urlopen


def main():
    r = Request('https://alx-intranet.hbtn.io/status')
    with urlopen(r) as f:
        html_file = f.read()
        print('Body response:')
        print('\t - type: {}'.format(type(html_file)))
        print('\t - content: {}'.format(html_file))
        print('\t - utf8 content: {}'.format(html_file.decode('utf8')))


if __name__ == '__main__':
    main()
