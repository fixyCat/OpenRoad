from pathlib import Path

import click
from rich.console import Console

from openroad.core.installer import copy_template_tree
from openroad.core.paths import resolve_project_root


console = Console()


@click.command()
@click.option(
    "--target",
    default="opencode",
    show_default=True,
    help="Target agent/tool template to initialize.",
)
@click.option(
    "--path",
    "project_path",
    default=None,
    help="Path to the project root. Defaults to current directory.",
)
@click.option(
    "--force",
    is_flag=True,
    help="Overwrite existing OpenRoad files.",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be changed without writing files.",
)
def init_command(
    target: str,
    project_path: str | None,
    force: bool,
    dry_run: bool,
) -> None:
    """Initialize OpenRoad files in a project."""
    project_root: Path = resolve_project_root(project_path)

    result = copy_template_tree(
        target=target,
        project_root=project_root,
        force=force,
        dry_run=dry_run,
    )

    heading = "OpenRoad initialization preview" if dry_run else "OpenRoad initialized"
    console.print(f"\n[bold]{heading}[/bold]")
    console.print(f"Project root: [cyan]{project_root}[/cyan]")
    console.print(f"Target: [cyan]{target}[/cyan]\n")

    if result.created:
        console.print("[green]Created:[/green]")
        for path in result.created:
            console.print(f"  {path}")

    if result.overwritten:
        console.print("\n[yellow]Overwritten:[/yellow]")
        for path in result.overwritten:
            console.print(f"  {path}")

    if result.skipped:
        console.print("\n[blue]Skipped existing files:[/blue]")
        for path in result.skipped:
            console.print(f"  {path}")

        if not force:
            console.print("\nUse [bold]--force[/bold] to overwrite existing files.")

    if not result.created and not result.overwritten and not result.skipped:
        console.print("[yellow]No files were copied.[/yellow]")

    console.print()