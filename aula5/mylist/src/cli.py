import click
import sys

@click.group()
def cli():
    pass

@cli.command()
@click.argument('item')
# @click.pass_context
def add(ctx, item):
    # Adicionar um item à lista de compras
    click.echo(f"Item '{item}' adicionado à lista de compras.")

@cli.command()
@click.argument('item')
# @click.pass_context
def remove(ctx, item):
    # Remover item da lista de compras
    click.echo(f"Item '{item}' removido da lista de compras.")

@cli.command()
# @click.pass_context
def export(ctx):
    # Exportar a lista de compras para um arquivo de texto
    with open('cli_list.txt', 'w') as f:
        f.write("Lista de compras exportada.")
    click.echo("Lista de compras exportada para cli_list.txt.")

if __name__ == '__main__':
    cli()

# @click.group()
# @click.option('---', default=False)
# @click.pass_context
# def cli(ctx, list):
#     # ensure that ctx.obj exists and is a dict (in case `cli()` is called
#     # by means other than the `if` block below)
#     ctx.ensure_object(list)

#     ctx.obj['append'] = list
