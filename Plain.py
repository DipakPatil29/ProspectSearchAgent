import yaml
from pathlib import Path


def load_icp_config(file_path):
    """
    Load ICP configuration from a YAML file.
    
    Args:
        file_path (str or Path): Path to the YAML configuration file
        
    Returns:
        dict: Configuration dictionary loaded from the YAML file
        
    Raises:
        FileNotFoundError: If the specified file does not exist
        yaml.YAMLError: If the file contains invalid YAML syntax
        PermissionError: If the file cannot be read due to permission issues
    """
    try:
        # Convert to Path object for better path handling
        config_path = Path(file_path)
        
        # Check if file exists
        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {file_path}"
            )
        
        # Check if it's a file (not a directory)
        if not config_path.is_file():
            raise ValueError(
                f"Path is not a file: {file_path}"
            )
        
        # Read and parse the YAML file
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config_data = yaml.safe_load(config_file)
        
        # Ensure we return a dictionary
        if config_data is None:
            return {}
        
        if not isinstance(config_data, dict):
            raise ValueError(
                f"Configuration file must contain a YAML dictionary, "
                f"got {type(config_data).__name__} instead"
            )
        
        return config_data
        
    except FileNotFoundError:
        # Re-raise FileNotFoundError with the original message
        raise
    except PermissionError as e:
        raise PermissionError(
            f"Permission denied when reading file: {file_path}"
        ) from e
    except yaml.YAMLError as e:
        raise yaml.YAMLError(
            f"Invalid YAML syntax in file {file_path}: {str(e)}"
        ) from e
    except Exception as e:
        raise RuntimeError(
            f"Unexpected error loading configuration from {file_path}: {str(e)}"
        ) from e


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
