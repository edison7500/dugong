import requests


headers = {
    'Authorization': 'Token ad1eb35acec4d816f868e95fef394f1285f3d26c',
}

s = requests.session()


res = s.get(url='http://www.jiaxin.im/api/opensource/', headers=headers)

data = res.json()

results = data.get('results', None)


def generator_author():
    for row in results:
        yield row['author']
