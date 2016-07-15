#!/usr/bin/env python
import click

from pastdoc.backend import start


@click.command()
@click.option('-p', '--path', nargs=1, type=click.Path(
    exists=True, file_okay=False, readable=True))
@click.option('-u', '--url', nargs=1, type=str)
def main(path, url):
    if not (path or url):
        raise click.BadParameter('You should provide path or url to repo')
    if url:
        raise NotImplementedError('Working with remote libraries is not supported. Yet.')
    if path:
        start(path)


if __name__ == '__main__':
    main()
