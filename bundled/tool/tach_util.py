from __future__ import annotations
from typing import TYPE_CHECKING

from tach.extension import check
from tach.parsing.config import parse_project_config
from tach.cli import parse_arguments
from tach.colors import BCOLORS
from tach.constants import CONFIG_FILE_NAME
from tach.errors import TachSetupError
from tach.filesystem import find_project_config_root

if TYPE_CHECKING:
    from tach.extension import CheckResult


def run_tach_check(argv: list[str], path: str):
    args, _ = parse_arguments(argv[1:])
    root = find_project_config_root()
    if not root:
        raise TachSetupError("Project config root not found")
    exclude_paths = args.exclude.split(",") if getattr(args, "exclude", None) else None
    project_config = parse_project_config(root=root)
    if project_config is None:
        raise TachSetupError(
            f"{BCOLORS.FAIL} {CONFIG_FILE_NAME}.(toml) not found in {root}{BCOLORS.ENDC}",
        )

    if exclude_paths is not None and project_config.exclude is not None:
        exclude_paths.extend(project_config.exclude)
    else:
        exclude_paths = project_config.exclude

    checked_result: CheckResult = check(
        project_root=root,
        project_config=project_config,
        dependencies=True,
        interfaces=False,
        exclude_paths=exclude_paths,
    )
    return checked_result
