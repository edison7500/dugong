from pprint import pprint
from time import sleep

import requests

headers = {
    'Authorization': 'Token ad1eb35acec4d816f868e95fef394f1285f3d26c',
}

s = requests.session()


def get_author(data):
    for row in data:
        yield row['author']


def get_results(url):
    res = s.get(url, headers=headers)
    next_url = res.json().get('next', None)
    data = res.json().get('results', None)
    return next_url, get_author(data)


def post_author(data):
    res = s.post(url='http://www.jiaxin.im/api/opensource/author/', json=data, headers=headers)
    return res.status_code


if __name__ == '__main__':
    star_url = 'http://www.jiaxin.im/api/opensource/'

    while True:
        # next_url = star_url
        next_url, data = get_results(url=star_url)
        for row in data:
            payload = {
                'author': row,
                'url': "https://github.com/{author}".format(author=row),
            }
            res = s.post(url='http://www.jiaxin.im/api/opensource/author/', json=payload, headers=headers)
            pprint(res.json(), indent=2)

        if next_url is None:
            break
        star_url = next_url
        sleep(5)
    # print (data)

    # for row in get_author(data):
    #     payload = {
    #         'author': row,
    #         'url': "https://github.com/{author}".format(author=row),
    #     }
    #     res = s.post(url='http://www.jiaxin.im/api/opensource/author/', json=payload, headers=headers)
