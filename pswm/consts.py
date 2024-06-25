from .cli import get_xdg_data_path

HELP_MSG = """
  pswm <alias> <user> <password>   - Store a username and a password.
  pswm <alias> <user> -g=<length>  - Store a random password for a username.
  pswm <alias> -d                  - Delete user and password for an alias.
  pswm <alias>                     - Print user and password for an alias.
  pswm -a                          - Print all stored users and passwords.
"""
MIN_PASS_LENGTH = 4
DEFAULT_PASS_LENGTH = 16
MAX_PASS_LENGTH = 32
PASS_VAULT_FILE = get_xdg_data_path("pswm")

informational = """
   - I M P O R T A N T -

1) You must have pswm installed in your '/usr/bin/' directory.

2) Your csv file must be formatted as below,
   which is the default for Chrome, Brave and other browsers:

   <name>,<url>,<username>,<password>

3) This script also needs to modify 'pswm' by replacing the line:

   crypt_key = getpass.getpass("[pswm] Master password: ")

   with:

   crypt_key = input("[pswm] Master password: ")

   It will be reverted back to normal when the insertion is finished.
   This is set to happen automatically but may fail in some cases.

   If you already did it manually, press 'M' in the following prompt.
   Otherwise, select 'A'.
"""

pswm_install = "/usr/bin/pswm"
old_l = 'crypt_key = getpass.getpass("[pswm] Master password: ")'
new_l = 'crypt_key = input("[pswm] Master password: ")'
