# pswm
A simple command line password manager written in python.


Built to be secure, it encrypts your passwords with a key that is not stored in any form.
![pswm](https://i.imgur.com/IqHqajs.png)

Its intuitive syntax and its reduced set of commands make it easy to use.
![pswm](https://i.imgur.com/GPNoxX6.png)

It looks better than you might expect for a command-line application thanks to the use of prettyTable.
![pswm](https://i.imgur.com/Ie5UCvX.png)

## Dependencies

pswm uses cryptocode & prettytable which can be installed through pip:

```
pip3 install cryptocode
pip3 install prettytable
```

It has been tested with Python 3.8.10. 
Results may vary if other versions are used.


## Installation

The following commands will download the latest version of pswm from this repository 
and install it in your `/usr/bin/` directory:
```
git clone https://github.com/Julynx/pswm
cd pswm
chmod +x pswm
sudo cp pswm /usr/bin/
```
The program can now be ran from a terminal with the command `pswm`.


## Usage

When running pswm for the first time, you will be prompted to define a master password which will be used to encrypt your other passwords. 

If you forget your master password, pswm will give you the option to reset it after three failed attempts. This would **delete** all your saved passwords, since they would be encrypted with your old master password and impossible to decrypt without it. You should store your master password somewhere safe or choose something you will always remember.

After choosing a master password, a password vault will be created as a file named `.pswm` inside your home folder, to store your encrypted passwords. You can use any of the following commands to access your password vault:
```
  pswm <alias> <username> <password>  - Store a username and a password.
  pswm <alias> <username> -g [length] - Generate a random password and store it.
  pswm <alias> -d                     - Delete user and password for an alias.
  pswm <alias>                        - Print user and password for an alias.
  pswm -a                             - Print all stored users and passwords.
```

## License

This software comes **without any warranty** as distributed under the GNU GPL 2.0 license.
You should receive a copy of the license with your download of pswm. 
The GNU GPL 2.0 license is available under the following url
https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html
