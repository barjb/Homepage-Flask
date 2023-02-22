from flask import request
poststemp = [{'id': 0, 'name': 'abc', 'tags': ['a', 'b']}, {'id': 1, 'name': 'bc', 'tags': ['b']}, {
    'id': 2, 'name': 'abc', 'tags': ['a', 'b', 'c']}, {'id': 3, 'name': 'abc', 'tags': ['a']}, {'id': 4, 'name': 'a', 'tags': ['a', 'b', 'c', 'd']}]


def all():
    if request.method == 'GET':
        return poststemp
    elif request.method == 'POST':
        name = request.json['name']
        tags = request.json['tags']
        id = len(poststemp)
        obj = {'id': id, 'name': name, 'tags': tags}
        poststemp.append(obj)
        return obj


def byid(id: int):
    if request.method == 'GET':
        return [post for post in poststemp if post['id'] == id]
    if request.method == 'DELETE':
        elem = filter(lambda e: e['id'] == id, poststemp)
        try:
            elem = next(elem)
            poststemp.remove(elem)
            return elem
        except StopIteration:
            return {}
    if request.method == 'PATCH':
        return 'ok'
    if request.method == 'PUT':
        return 'ok'


def bytag(tag: str):
    return [post for post in poststemp if tag in post['tags']]
