from pathlib import Path
from typing import Any


REQUIRED_FILES_OPENCODE = [
    {
        "path": "AGENTS.md",
        "type": "agent_instructions",
    },
    {
        "path": "openroad/roadmap.md",
        "type": "roadmap",
    },
    {
        "path": ".opencode/command/openroad.md",
        "type": "opencode_command",
    },
    {
        "path": ".opencode/command/openroad-close.md",
        "type": "opencode_command",
    },
]


def build_status(project_root: Path) -> dict[str, Any]:
    required = []

    for item in REQUIRED_FILES_OPENCODE:
        relative_path = item["path"]
        exists = (project_root / relative_path).exists()

        required.append(
            {
                "path": relative_path,
                "exists": exists,
                "type": item["type"],
            }
        )

    missing = [item["path"] for item in required if not item["exists"]]

    roadmap_path = project_root / "openroad" / "roadmap.md"
    roadmap_exists = roadmap_path.exists()

    initialized = len(missing) == 0

    recommendations = []

    if not initialized:
        recommendations.append(
            {
                "code": "RUN_INIT",
                "message": "Run openroad init to initialize this repository.",
            }
        )

    return {
        "schema_version": "0.1",
        "project_root": str(project_root),
        "initialized": initialized,
        "target": "opencode" if initialized else None,
        "files": {
            "required": required,
            "missing": missing,
        },
        "roadmap": {
            "exists": roadmap_exists,
            "path": "openroad/roadmap.md",
            "items_total": 0,
            "items_open": 0,
            "items_done": 0,
        },
        "recommendations": recommendations,
    }