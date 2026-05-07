import click

from openroad.commands.init import init_command
from openroad.commands.status import status_command


@click.group()
@click.version_option()
def cli() -> None:
    """OpenRoad project coordination CLI."""
    pass


cli.add_command(init_command, name="init")
cli.add_command(status_command, name="status")