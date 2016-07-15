from pastdoc.traverser import traverse
from pastdoc.walker import walk_over


def construct_inner(row):
    return {
        "nesting": row[0],
        "name": row[1],
        "docstring": row[2],
        "lineno": row[3]
    }


def construct_entry(name, content):
    return {
        'name': name,
        'content': content
    }


def start(entry):
    result = []
    for name, path in walk_over(entry):
        with open(path) as fp:
            content = fp.read()

        bucket = traverse(content)
        content = []
        for row in bucket:
            element = construct_inner(row)
            content.append(element)
        result.append(construct_entry(name, content))
    return result
