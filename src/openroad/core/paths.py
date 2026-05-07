from pathlib import Path


def resolve_project_root(path: str | None = None) -> Path:
    """Resolve the target project root.

    For now this simply resolves the supplied path or current directory.
    Later this can detect git roots.
    """
    if path:
        return Path(path).expanduser().resolve()

    return Path.cwd().resolve()