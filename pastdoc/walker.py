import os


def make_package(dirname):
    dirname = dirname or ''
    dirname = dirname.lstrip('./')
    dirname = dirname.replace('/', '.')
    return dirname


def trim_extension(filename):
    filename, _ = os.path.splitext(filename)
    return filename


def to_module(dirname, filename):
    dirname = make_package(dirname)
    filename = trim_extension(filename)
    return '.'.join([dirname, filename])


def is_good_dir(dirname):
    if dirname.startswith('.'):
        return False
    if dirname.find('-') != -1:
        return False
    return True


def walk_over(entry):
    entry = os.path.abspath(entry)
    prefix, module = os.path.split(entry)
    if not module:
        prefix, module = os.path.split(module)
    prefix_len = len(prefix)

    for dirpath, dirs, filenames in os.walk(entry):
        dirs[:] = [d for d in dirs if is_good_dir(d)]
        dirprefix = dirpath[prefix_len:]
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext != '.py':
                continue

            yield to_module(dirprefix, filename), os.path.join(dirpath, filename)
