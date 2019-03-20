#!/bin/bash

# Lints for syntastic.
pip3 install mypy --user
pip3 install pylint --user
pip3 install flake8 --user

# Testing.
pip3 install pytest --user

# For vim bar.
pip3 install powerline-status --user

# For neovim python support (YCM etc.)
pip3 install neovim --user --upgrade
