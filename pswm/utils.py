import os

from colorama import Fore, Style

from .consts import informational, new_l, old_l, pswm_install
from .models import Field, Mode


def replace(filename, old_line, new_line):
    """
    Replaces old_line with new_line in filename.

    Args:
        filename (str): Name of the file to perform the replacement on.
        old_line (str): Text to replace.
        new_line (str): Text to replace with.
    """
    wlines = []
    with open(filename, "r") as readfile:
        lines = readfile.readlines()
        for line in lines:
            if old_line in line:
                line = line.replace(old_line, new_line)
            wlines.append(line)

    with open(filename, "w") as writefile:
        writefile.writelines(wlines)


def restore(filename, old_line, new_line):
    """
    Replaces new_line with old_line in filename.

    Args:
        filename (str): Name of the file to perform the replacement on.
        old_line (str): Text to replace with.
        new_line (str): Text to replace.
    """
    wlines = []
    with open(filename, "r") as readfile:
        lines = readfile.readlines()
        for line in lines:
            if new_line in line:
                line = line.replace(new_line, old_line)
            wlines.append(line)

    with open(filename, "w") as writefile:
        writefile.writelines(wlines)


def simplify(name):
    """
    Gets rid of leading strings like 'www.'
    and trailing strings like '.com'.

    Args:
        name (str): Url to simplify.

    Returns:
        str: Simplified url.
    """
    if name.startswith("www."):
        ename = name.replace("www.", "")
    else:
        ename = name

    words = ename.split(".")
    ename = words[len(words) - 2]

    return ename


def check_format(line):
    """
    Checks if the line is correctly formatted.

    Args:
        line (str): Line to be checked.

    Returns:
        Boolean: True if the line is correctly formatted, False otherwise.
    """
    if len(line.split(",")) != 4 or line.startswith("name"):
        print("")
        print(Fore.RED + "Skipping invalid line:")
        print(line, end="")
        print(Style.RESET_ALL)
        return False
    return True


def from_csv(filename, master_password):
    # Informational prompt
    print(informational)
    choice: str = input("([A]uto / [M]anual / [Q]uit) Enter your choice: ")
    if choice in Mode.QUIT.value:
        print("\nAborted.\n")
        exit(0)

    # Automatic replacement
    if choice not in Mode.MANUAL.value:
        replace(pswm_install, old_line=old_l, new_line=new_l)

    # Read the csv file
    with open(filename, "r") as file:
        lines = file.readlines()

    # Import each password in the csv file
    for line in lines:
        if not check_format(line):
            continue

        words = line.split(",")

        name = simplify(words[Field.NAME.value])
        _ = words[Field.URL.value]
        user = words[Field.USER.value]
        passw = words[Field.PASS.value]

        command = " ".join(["echo", master_password, "|", "pswm", name, user, passw])

        os.system(command)

    # Automatic restoration
    if choice not in Mode.MANUAL.value:
        restore(pswm_install, old_line=old_l, new_line=new_l)

    # Print success message
    print(Fore.GREEN + "\n- SUCCESS -\n")
