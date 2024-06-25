import getpass
import os
import random
import string

import cryptocode
from prettytable import SINGLE_BORDER, PrettyTable

from .consts import MAX_PASS_LENGTH, MIN_PASS_LENGTH, PASS_VAULT_FILE


def print_pass_vault(pass_vault, alias=None):
    """
    Function to print the password vault using prettyTable.

    Args:
        pass_vault (dict): A dictionary of aliases associated to usernames
        and passwords.
        alias (str, optional): The alias to print.
        If None, all aliases are printed. Defaults to None.
    """
    if len(pass_vault) == 0:
        print("The password vault is empty.")
        return

    table = PrettyTable()
    if alias is not None:
        if alias in pass_vault:
            row = []
            row.append(alias)
            row.extend(pass_vault[alias])
            table.add_row(row)
        else:
            print("No password for " + alias + " was found.")
            return
    else:
        for stored_alias in sorted(pass_vault, key=lambda x: x[0].lower()):
            row = []
            row.append(stored_alias)
            row.extend(pass_vault[stored_alias])
            table.add_row(row)

    table.field_names = ["Alias", "Username", "Password"]
    table.align = "l"
    table.set_style(SINGLE_BORDER)
    print(table)


def register():
    """
    This function asks the user for a master password for the creation of a
    password vault.

    Returns:
        str, list: The master password and a list of lines containing the
        aliases, users and passwords for the password vault.
    """
    crypt_key = ""
    while len(crypt_key) < MIN_PASS_LENGTH or len(crypt_key) > MAX_PASS_LENGTH:
        try:
            crypt_key = getpass.getpass(
                "[pswm] Create a master password ("
                + str(MIN_PASS_LENGTH)
                + "-"
                + str(MAX_PASS_LENGTH)
                + " chars): "
            )
        except KeyboardInterrupt:
            print("\n")
            return False, ""

    crypt_key_verify = ""
    while crypt_key_verify != crypt_key:
        try:
            crypt_key_verify = getpass.getpass(
                "[pswm] Confirm your " "master password: "
            )
        except KeyboardInterrupt:
            print("\n")
            return False, ""

    print("Password vault ~/.pswm created.")
    lines = []
    lines.append("pswm\t" + getpass.getuser() + "\t" + crypt_key)
    return crypt_key, lines


def login():
    """
    This function decrypts and reads the password vault.

    Returns:
        str, list: The master password and a list of lines containing the
        aliases and passwords decrypted from the password vault.
    """
    for _ in range(3):

        try:
            crypt_key = getpass.getpass("[pswm] Master password: ")
        except KeyboardInterrupt:
            print("\n")
            return False, ""

        lines = encrypted_file_to_lines(PASS_VAULT_FILE, crypt_key)
        if not lines:
            print("Sorry, try again.")
        else:
            return crypt_key, lines

    print("\nYou have failed to enter the master password 3 times.")
    return reset_master_password()


def manage_master_password():
    """
    Manager function for the master password. Asks the user for the master
    password if there is already a password vault. If not, it creates a new
    password vault associated to a new master password. Can also reset the
    master password after 3 failed attempts.

    Returns:
        str, list: The master password and a list of lines containing the
        aliases and passwords decrypted from the password vault.
    """
    if not (os.path.isfile(PASS_VAULT_FILE) and os.path.getsize(PASS_VAULT_FILE) > 0):
        return register()
    return login()


def reset_master_password():
    """
    Function to reset the master password.

    Returns:
        str, list: The master password and a list of lines containing the
        aliases and passwords decrypted from the password vault.
    """
    print("Resetting your master password will delete your password vault.")
    try:
        text = input("[pswm] Do you want to reset your master password? (y/n): ")
    except KeyboardInterrupt:
        print("\nPassword reset aborted.")
        return False, ""

    if text == "y":
        if os.path.isfile(PASS_VAULT_FILE):
            os.remove(PASS_VAULT_FILE)
            print("Password vault ~/.pswm deleted.\n")
        return manage_master_password()

    print("Password reset aborted.")
    return False, ""


def lines_to_pass_vault(lines):
    """
    Splits each line of a list of lines into two parts. Then inserts the second
    part into the dictionary indexed by the first part.

    Args:
        lines(list): A list of lines.

    Returns:
        dict: A dictionary containing the aliases, usernames and passwords.
    """
    pass_vault = {}
    for line in lines:
        line = line.rstrip()
        try:
            alias, username, password = line.split("\t")
            pass_vault[alias] = [username, password]
        except ValueError:
            pass

    return pass_vault


def pass_vault_to_lines(pass_vault):
    """
    For each key in the dictionary, it inserts a string into a list containing
    the key and the values separated by a tab.

    Args:
        pass_vault(dict): A dictionary aliases associated to usernames
        and passwords.

    Returns:
        list: A list of lines each formatted as key\tvalue[0]\tvalue[1].
    """
    lines = [
        "\t".join([alias, pass_vault[alias][0], pass_vault[alias][1]])
        for alias in pass_vault
    ]

    return lines


def encrypted_file_to_lines(file_name, master_password):
    """
    This function opens and decrypts the password vault.

    Args:
        file_name (str): The name of the file containing the password vault.
        master_password (str): The master password to use to decrypt the
        password vault.

    Returns:
        list: A list of lines containing the decrypted passwords.
    """
    if not os.path.isfile(file_name):
        return ""

    with open(file_name, "r") as file:
        encrypted_text = file.read()

    decrypted_text = cryptocode.decrypt(encrypted_text, master_password)
    if decrypted_text is False:
        return False

    decrypted_lines = decrypted_text.splitlines()
    return decrypted_lines


def lines_to_encrypted_file(lines, file_name, master_password):
    """
    This function encrypts and stores the password vault.

    Args:
        lines (list): A list of lines containing the aliases and passwords.
        file_name (str): The name of the file to store the password vault.
        master_password (str): The master password to use to encrypt the
        password vault.
    """
    decrypted_text = "\n".join(lines)
    encrypted_text = cryptocode.encrypt(decrypted_text, master_password)

    with open(file_name, "w") as file:
        file.write(encrypted_text)


def generate_password(length):
    """
    This function generates a random password of length passed as argument.

    Args:
        length (int): The length of the random password to be generated.

    Returns:
        str: A string containing the random password.
    """
    characters = string.ascii_letters + string.digits + "%+,-./:=@^_{}~"
    return "".join(random.choice(characters) for _ in range(length))
