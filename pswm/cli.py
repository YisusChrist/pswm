import os
import sys
from contextlib import suppress


def _get_xdg_path(env: str, app: str, default: str, create: bool = False) -> str:
    """
    Returns the value of the env environment variable with
    the app folder and file appended to it. (See example below)

    Example: Return value equals to
             "XDG_CONFIG_HOME/app/app"
             or
             "default/app/app" if XDG_CONFIG_HOME is not set

    Args:
        env (str): Name of the environment variable.
        app (str): Name of the app to be used for the folder and the file.
        default (str): Default value to use for the path if env
        is not set.
        create (bool): Wether to create the config file or not.
        Defaults to False. Dirs are always created if they don't exist.

    Returns:
        str: Path to the app folder and file or fallback value.
    """

    # 1. Read the XDG_config environment variable
    if env in os.environ and os.path.exists(os.environ[env]):
        config = os.environ[env]
    else:
        # Expand the default path
        config = os.path.expanduser(default)

    config = config[:-1] if config.endswith("/") else config

    # 2. Create the app folder if it doesn't exist
    config += f"/{app}"
    os.makedirs(config, exist_ok=True)

    # 3. Add the config file name to the path
    config += f"/{app}"
    if not os.path.exists(config) and create:
        with open(config, "w") as file:
            file.write("")

    return config


def get_xdg_data_path(app: str, create: bool = False) -> str:
    """
    Returns the value of the XDG_DATA_HOME environment variable with
    the app folder and file appended to it. (See example below)

    Example: Return value equals to
            "XDG_DATA_HOME/app/app"
            or
            "default/app/app" if XDG_DATA_HOME is not set

    Args:
        app (str): Name of the app to be used for the folder and the file.
        create (bool, optional): Wether to create the config file or not.
        Defaults to False. Dirs are always created if they don't exist.

    Returns:
        str: path to the app folder and file or fallback value.
    """
    return _get_xdg_path(
        env="XDG_DATA_HOME", app=app, default="~/.local/share", create=create
    )


def args(positional=None):
    """
    Simple argument parser.

    Example:
    $: program joe 1234 -keep -host=127.0.0.1

    dictionary = args(["username", "password"])

    >> username:    joe
    >> password:    1234
    >> -keep:       True
    >> -host:       127.0.0.1

    Args:
        positional (str): A list of strings for the positional arguments.

    Returns:
        dict: A dictionary containing the argument names and their values.
    """
    positional = [] if positional is None else positional
    args_dict = {}

    # Store positional arguments
    tail = len(positional)
    for i, pos_arg in enumerate(positional):
        with suppress(IndexError):
            if str(sys.argv[i + 1]).startswith("-"):
                tail = i
                break
            value = sys.argv[i + 1]
            args_dict[pos_arg] = value

    # Store flags
    for i in range(tail + 1, len(sys.argv)):
        try:
            value = str(sys.argv[i]).split("=")[1]
        except IndexError:
            value = True
        args_dict[str(sys.argv[i]).split("=", maxsplit=1)[0]] = value

    return args_dict
