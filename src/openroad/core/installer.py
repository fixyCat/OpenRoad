from dataclasses import dataclass
from importlib.resources import files
from pathlib import Path
import shutil


@dataclass
class InstallResult:
    created: list[str]
    skipped: list[str]
    overwritten: list[str]


def get_template_root(target: str) -> Path:
    template_root = files("openroad").joinpath("markdowns", target)

    # importlib.resources returns Traversable, but shutil wants paths.
    # This works when running from source. For packaged wheels, we may need
    # as_file later.
    return Path(str(template_root))


def copy_template_tree(
    *,
    target: str,
    project_root: Path,
    force: bool = False,
    dry_run: bool = False,
) -> InstallResult:
    template_root = get_template_root(target)

    if not template_root.exists():
        raise ValueError(f"Unknown target template: {target}")

    created: list[str] = []
    skipped: list[str] = []
    overwritten: list[str] = []

    for source_path in template_root.rglob("*"):
        if source_path.is_dir():
            continue

        relative_path = source_path.relative_to(template_root)
        destination_path = project_root / relative_path
        display_path = str(relative_path)

        if destination_path.exists():
            if force:
                overwritten.append(display_path)
                if not dry_run:
                    destination_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(source_path, destination_path)
            else:
                skipped.append(display_path)
            continue

        created.append(display_path)

        if not dry_run:
            destination_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, destination_path)

    return InstallResult(
        created=created,
        skipped=skipped,
        overwritten=overwritten,
    )