from __future__ import annotations

from tach.check import CheckResult, check
from tach.cli import parse_arguments
from tach.colors import BCOLORS
from tach.constants import CONFIG_FILE_NAME
from tach.errors import TachSetupError
from tach.filesystem import find_project_config_root
from tach.parsing import parse_project_config


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
        project_root=root, project_config=project_config
    )
    for boundary_error in checked_result.errors:
        # Hack for now - update error message displayed to user
        error_info = boundary_error.error_info
        if (
            not error_info.exception_message
            and boundary_error.error_info.is_dependency_error
        ):
            error_info.exception_message = (
                f"Cannot import '{boundary_error.import_mod_path}'. "
                f"Module '{error_info.source_module}' cannot depend on '{error_info.invalid_module}'."
            )
    return checked_result
