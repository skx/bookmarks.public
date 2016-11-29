#!/usr/bin/env python3

"""
Pinboard to bookmarks.public importer

Requires:
* Python 3.5
* Requests: <http://python-requests.org/>
"""

import json
from os.path import join, dirname, realpath

import requests

PINBOARD_API_ENDPOING = ('https://api.pinboard.in/v1/{method}'
                         '?auth_token={api_token}&format=json')
BOOKMARK_PUBLIC_TPL = ('<li title="{tags}"><a href="{href}">'
                       '{description}</a></li>\n')


def get_bookmarks(api_token):
    resp = requests.get(PINBOARD_API_ENDPOING.format(method='posts/all',
                                                     api_token=api_token))

    if not resp.status_code == 200:
        raise Exception

    return resp.json()


def write_data_file(bookmarks, filename):
    with open(filename, 'w') as fobj:
        for bookmark in bookmarks:
            if not bookmark['shared'] == 'yes':
                continue

            if bookmark['description'].startswith('(404) '):
                continue

            if bookmark['description'] == '':
                bookmark['description'] = bookmark['href']

            bookmark['tags'] = ', '.join(bookmark['tags'].split(' '))

            fobj.write(BOOKMARK_PUBLIC_TPL.format(**bookmark))


def main(api_token):
    bookmarks = get_bookmarks(api_token)

    bookmarks_data_file = join(dirname(realpath(__file__)),
                               '../../bookmarks.data')

    write_data_file(bookmarks, bookmarks_data_file)


if __name__ == '__main__':
    print('Copy your API Token from <https://pinboard.in/settings/password>.')
    print('And paste it below.')
    api_token = input('API Token: ')

    main(api_token)
