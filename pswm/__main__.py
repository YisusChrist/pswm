from .cli import args
from .consts import DEFAULT_PASS_LENGTH, HELP_MSG, PASS_VAULT_FILE
from .vault import (
    generate_password,
    lines_to_encrypted_file,
    lines_to_pass_vault,
    manage_master_password,
    pass_vault_to_lines,
    print_pass_vault,
)


def main():
    """
    Main function.
    """
    crypt_key, lines = manage_master_password()
    if not crypt_key:
        return

    pass_vault = lines_to_pass_vault(lines)
    arg = args(["site", "username", "password"])

    if ("password" in arg or "-g" in arg or "-d" in arg) and (
        str(arg.get("site", "")) == "pswm"
    ):
        print("You cannot change or delete the master password.")

    elif arg.keys() == {"site", "username", "password"}:
        pass_vault[arg["site"]] = [arg["username"], arg["password"]]
        print("Added username and password for " + arg["site"] + ".")

    elif arg.keys() == {"site", "username", "-g"}:
        try:
            length = int(arg["-g"])
            if length <= 4:
                raise ValueError
        except ValueError:
            length = DEFAULT_PASS_LENGTH
        pass_vault[arg["site"]] = [arg["username"], generate_password(length)]
        print_pass_vault(pass_vault, arg["site"])

    elif arg.keys() == {"site", "-d"}:
        try:
            del pass_vault[arg["site"]]
            print("Deleted username and password for " + arg["site"] + ".")
        except KeyError:
            print("No password found for " + arg["site"] + ".")

    elif arg.keys() == {"site"}:
        print_pass_vault(pass_vault, arg["site"])

    elif arg.keys() == {"-a"}:
        print_pass_vault(pass_vault)

    else:
        print(HELP_MSG)

    lines = pass_vault_to_lines(pass_vault)
    lines_to_encrypted_file(lines, PASS_VAULT_FILE, crypt_key)


if __name__ == "__main__":
    main()
