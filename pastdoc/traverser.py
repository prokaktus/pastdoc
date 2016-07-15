import ast


def nesting(f):
    def wrapper(self, *args, **kwargs):
        self.nesting_level += 1
        res = f(self, *args, **kwargs)
        self.nesting_level -= 1
        return res
    return wrapper


class Traverser(ast.NodeVisitor):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nesting_level = 0

    @property
    def bucket(self):
        return self._bucket

    def _extract_docstring(self, node):
        docstring = ast.get_docstring(node)
        self._bucket.append((self.nesting_level, node.name, docstring, node.lineno))
        return self._bucket

    @nesting
    def visit_FunctionDef(self, node):
        self._extract_docstring(node)
        self.generic_visit(node)

    @nesting
    def visit_ClassDef(self, node):
        self._extract_docstring(node)
        self.generic_visit(node)

    @nesting
    def visit_AsyncFunctionDef(self, node):
        self._extract_docstring(node)
        self.generic_visit(node)

    def visit_Module(self, node):
        self._bucket = []
        self.generic_visit(node)


def traverse(src):
    parsed = ast.parse(src)
    t = Traverser()
    t.visit(parsed)
    bucket = t.bucket
    return bucket
