import click
import os

filename = "COMPRAS.txt"

@click.command()
def hello():
    click.echo("Hello", color=True)

@click.command()
@click.argument("product")
def add(product:str):
    breakpoint()
    file =open(filename, "w")
    file.write(f"{product}\n")
    file.close()
    click.echo(f"{product.upper()}added!")

    
    # with open(filename, "w") as file:
    #     products = file.readlines()
    #     products.append(product)
    #     file.write("\n".join(products))



if __name__ == '__main__':
    hello()