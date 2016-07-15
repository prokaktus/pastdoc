from pastdoc.traverser import traverse
from pastdoc.walker import walk_over


def start(entry):
    for name, path in walk_over(entry):
        pass
