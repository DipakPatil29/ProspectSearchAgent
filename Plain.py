##The general check
print("Hello WOrld!!")

from typing import Any, Dict

import yaml


def load_icp_config(file_path: str) -> Dict[str, Any]:
    """
    Load ICP configuration from a YAML file using PyYAML.

    Args:
        file_path: Path to the YAML configuration file.

    Returns:
        Dictionary with the parsed configuration. Returns an empty dict if the file is empty.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the YAML root is not a mapping/dictionary.
        yaml.YAMLError: If the YAML content is malformed.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"ICP configuration file not found: {file_path}") from exc

    if content is None:
        return {}
    if not isinstance(content, dict):
        raise ValueError("ICP configuration must be a mapping/dictionary at the root")

    return content
