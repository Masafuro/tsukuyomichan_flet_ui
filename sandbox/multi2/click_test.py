import click

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def greet(name):
    click.echo(f"Hello, {name}!")

@cli.command()
def goodbye():
    click.echo("Goodbye!")

if __name__ == "__main__":
    cli()
