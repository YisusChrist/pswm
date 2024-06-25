<p align="center"><img width="750" src="https://i.imgur.com/IqHqajs.png" alt="pswm"></p>

<p align="center">
    <a href="https://github.com/YisusChrist/pswm/issues">
        <img src="https://img.shields.io/github/issues/YisusChrist/pswm?color=171b20&label=Issues%20%20&logo=gnubash&labelColor=e05f65&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pswm/forks">
        <img src="https://img.shields.io/github/forks/YisusChrist/pswm?color=171b20&label=Forks%20%20&logo=git&labelColor=f1cf8a&logoColor=ffffff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pswm/">
        <img src="https://img.shields.io/github/stars/YisusChrist/pswm?color=171b20&label=Stargazers&logo=octicon-star&labelColor=70a5eb">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pswm/actions">
        <img alt="Tests Passing" src="https://github.com/YisusChrist/pswm/actions/workflows/github-code-scanning/codeql/badge.svg">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://github.com/YisusChrist/pswm/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/YisusChrist/pswm?color=0088ff">&nbsp;&nbsp;&nbsp;
    </a>
    <a href="https://opensource.org/license/gpl-2-0/">
        <img alt="License" src="https://img.shields.io/github/license/YisusChrist/pswm?color=0088ff">
    </a>
</p>

<br>

<p align="center">
    <a href="https://github.com/YisusChrist/pswm/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/YisusChrist/pswm/issues/new/choose">Request Feature</a>
    ·
    <a href="https://github.com/YisusChrist/pswm/discussions">Ask Question</a>
    ·
    <a href="https://github.com/YisusChrist/pswm/security/policy#reporting-a-vulnerability">Report security bug</a>
</p>

<br>

![Alt](https://repobeats.axiom.co/api/embed/d555a3fbabf737a912e20f8bef93fe9285e76417.svg "Repobeats analytics image")

<br>

Built to be secure, it encrypts your passwords with a key that only you know. Its intuitive syntax and reduced set of commands make it easy to use.

<details>
<summary>Table of Contents</summary>

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Importing from CSV](#importing-from-csv)
- [License](#license)
- [Credits](#credits)

</details>

<h4 align="center">It looks better than you might expect for a command-line application thanks to prettytable.</h4>
<p align="center">  
  <img width="772" src="https://i.imgur.com/Ie5UCvX.png">
</p>

# Requirements

Here's a breakdown of the packages needed and their versions:

- [poetry](https://pypi.org/project/poetry) - 1.8.3 (_only for manual installation_)
- [cryptocode](https://pypi.org/project/cryptocode) - 0.1
- [prettytable](https://pypi.org/project/prettytable) - 3.10.0
- [rich](https://pypi.org/project/rich) - 13.7.1

> [!NOTE]
> The software has been developed and tested using Python `3.12.1`. The minimum required version to run the software is Python 3.6. Although the software may work with previous versions, it is not guaranteed.

# Installation

`pswm` can be installed easily as a PyPI package. Just run the following command:

```bash
pip3 install pswm
```

> [!IMPORTANT]
> For best practices and to avoid potential conflicts with your global Python environment, it is strongly recommended to install this program within a virtual environment. Avoid using the --user option for global installations. We highly recommend using [pipx](https://pypi.org/project/pipx) for a safe and isolated installation experience. Therefore, the appropriate command to install `pswm` would be:
>
> ```bash
> pipx install pswm
> ```

The program can now be ran from a terminal with the `pswm` command.

# Usage

When running pswm for the first time, you will be prompted to define a master password that will be used to encrypt your other passwords.

If you forget your master password, pswm will give you the option to reset it after three failed attempts. This would **delete** all your saved passwords since they would be encrypted with your old master password and impossible to decrypt without it. You should store your master password somewhere safe or choose something you will always remember.

After choosing a master password, a password vault will be created as an encrypted file named `pswm` inside `~/.local/share/pswm/`.
You can use any of the following commands to access your password vault:

![Alt](https://i.imgur.com/9CiNNiz.png "pswm commands")

# Importing from CSV

You can use the included python script `from_csv.py` to import passwords from your browser into pswm:

- In Chrome, navigate to `Settings > Autofill > Passwords`.
- Click on the three dotted menu to the right of _Saved Passwords_ and select `Export passwords`.
- You can now execute the script to import all your passwords into pswm with the following command:

```
python3 from_csv.py <file.csv> <master_password>
```

# License

This software comes **without any warranty** as distributed under the [GNU GPL 2.0 license](https://www.gnu.org/licenses/old-licenses/gpl-2.0-standalone.html).

You should receive a copy of the license with your download of pswm.

# Credits

> [!NOTE]
> Credits to [Julynx](https://github.com/Julynx) for creating the script. I only make improvements in his code based on my preferences to customize it. All the ideas and the base of the script are his.
