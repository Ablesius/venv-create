#! /usr/bin/env python3
"""Create a virtualenv, python version and write .python-version file"""
import os
import subprocess
from typing import List
from sys import argv, exit


def create_venv(python_version: str):
    def concat_venv_name(python_version: str):
        current_dir = os.path.basename(os.getcwd())
        return f"{current_dir}-{python_version}"

    venv_name = concat_venv_name(python_version)
    subprocess.run(['pyenv', 'virtualenv', python_version, venv_name])
    return venv_name


def install_python_version(version: str):
    subprocess.run(['pyenv', 'install', '--skip-existing', version])


def _read_version_file():
    with open('.python-version', mode='r') as f:
        content = f.read()
        f.seek(0)
    return content.strip()


def write_to_version_file(venv_name: str):
    try:
        with open('.python-version', 'x') as f:
           f.write(venv_name)
    except FileExistsError:
        print(f".python-version already exists with version {_read_version_file()}")
        exit(1)


if __name__ == '__main__':
    python_version = argv[1]
    # normal calls:
    # mkcd $new_dir oder git clone foo; this will be required before.
    # cd into the directory before you run the script.

    # pyenv install -s $version # --skip-existing
    install_python_version(python_version)

    # pyenv virtualenv $version ${new_dir}-${version}
    venv_name = create_venv(python_version)

    # if not .python-version: echo ${new_dir}-${version} > .python-version
    write_to_version_file(venv_name)
