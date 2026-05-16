import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from openroad.core.paths import resolve_project_root
from openroad.core.status import build_status


console = Console()


@click.command()
@click.option(
    "--json",
    "as_json",
    is_flag=True,
    help="Output machine-readable JSON.",
)
@click.option(
    "--path",
    "project_path",
    default=None,
    help="Path to the project root. Defaults to current directory.",
)
def status_command(as_json: bool, project_path: str | None) -> None:
    """Show OpenRoad status for the current project."""
    project_root: Path = resolve_project_root(project_path)
    status = build_status(project_root)

    if as_json:
        click.echo(json.dumps(status, indent=2))
        return

    console.print("\n[bold]OpenRoad status[/bold]\n")
    console.print(f"Project root: [cyan]{status['project_root']}[/cyan]")
    console.print(f"Initialized: [cyan]{status['initialized']}[/cyan]")
    console.print(f"Target: [cyan]{status['target']}[/cyan]\n")

    table = Table(title="Required files")
    table.add_column("Path")
    table.add_column("Exists")
    table.add_column("Type")

    for item in status["files"]["required"]:
        exists_label = "[green]yes[/green]" if item["exists"] else "[red]no[/red]"
        table.add_row(item["path"], exists_label, item["type"])

    console.print(table)

    if status["recommendations"]:
        console.print("\n[yellow]Recommendations:[/yellow]")
        for recommendation in status["recommendations"]:
            console.print(f"  {recommendation['code']}: {recommendation['message']}")

    console.print()