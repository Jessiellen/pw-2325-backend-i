import sys
import click

@click.group
def cli():
    pass
    

@cli.command()
@click.argument("name")
def run(name:str):
    print(f"Hi {name}!")
    
if __name__ == '__main__':
    name = sys.argv[1]
  
    run(name=name)
    

# @click.group()
# @click.option('---', default=False)
# @click.pass_context
# def cli(ctx, list):
#     # ensure that ctx.obj exists and is a dict (in case `cli()` is called
#     # by means other than the `if` block below)
#     ctx.ensure_object(list)

#     ctx.obj['append'] = list