import click

@click.command()
@click.option('--name', '-n', default='World', help='Name to greet')
def hello(name):
    click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()

