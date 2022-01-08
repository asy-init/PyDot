import sqlite3
import click


@click.command()
@click.option("-a", "--add", default=None, help="add directory to tracker")
@click.option("-rm", "--remove", default=None, help="remove directory from tracker")
def cli(add, remove):
    """PyDot is an intivative terminal bsaed dotfile manager"""

    if add != None:
        click.echo("add!")
    if remove != None:
        click.echo("rm")
    click.echo(f"{add}, {remove} ")
