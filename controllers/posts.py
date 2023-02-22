from flask import request
poststemp = [{'id': 0, 'name': 'abc', 'tags': ['a', 'b']}, {'id': 1, 'name': 'bc', 'tags': ['b']}, {
    'id': 2, 'name': 'abc', 'tags': ['a', 'b', 'c']}, {'id': 3, 'name': 'abc', 'tags': ['a']}, {'id': 4, 'name': 'a', 'tags': ['a', 'b', 'c', 'd']}]


def all():
    if request.method == 'GET':
        return poststemp
    elif request.method == 'POST':
        try:
            name = request.json['name']
            tags = request.json['tags']
        except:
            return {}
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
        tags = None
        name = None
        try:
            name = request.json['name']
        except:
            pass
        try:
            tags = request.json['tags']
        except:
            pass
        obj = {'id': id}
        elem = filter(lambda e: e['id'] == id, poststemp)
        try:
            elem = next(elem)
            poststemp.remove(elem)
        except StopIteration:
            pass
        if name:
            obj['name'] = name
        else:
            obj['name'] = elem['name']
        if tags:
            obj['tags'] = tags
        else:
            obj['tags'] = elem['tags']
        poststemp.insert(id, obj)
        return obj
    if request.method == 'PUT':
        name = request.json['name']
        tags = request.json['tags']
        obj = {'id': id, 'name': name, 'tags': tags}
        elem = filter(lambda e: e['id'] == id, poststemp)
        try:
            elem = next(elem)
            poststemp.remove(elem)
        except StopIteration:
            pass
        poststemp.insert(id, obj)
        return obj


def bytag(tag: str):
    return [post for post in poststemp if tag in post['tags']]
