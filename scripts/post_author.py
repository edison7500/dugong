import requests


headers = {
    'Authorization': 'Token ad1eb35acec4d816f868e95fef394f1285f3d26c',
}

s = requests.session()


def get_author(url=None):
    if url is None:
        return
    # res = s.get(url='http://www.jiaxin.im/api/opensource/', headers=headers)
    res = s.get(url=url, headers=headers)
    data = res.json()

    for row in data.get('results', []):
        yield row['author']
    # yield get_author(data.get('next'))

    # return data.get('results')
    # data = res.json()
    # results = data.get('results', None)
    # next_url = data.get('next', None)
    #
    #
    #
    # yield s.get(next_url, headers=headers)

for row in get_author('http://www.jiaxin.im/api/opensource/'):
    print (row)

# def get_data():

    # get_author()

# def generator_author():
#
#     for row in results:
#         yield row['author']
#
#
# for row in generator_author():
#     data = {
#         'author': row,
#         'url': "https://github.com/{author}".format(author=row),
#     }
#     res = s.post(url='http://www.jiaxin.im/api/opensource/author/', json=data, headers=headers)
#     print (res.json())