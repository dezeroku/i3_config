#!/bin/sh

# Update repo.
git pull

# Symlink dotfiles.
python3 setup.py setup --symlink-dotfiles ../setup/dotfiles/ ~/backup_dotfiles

# Install stuff for Go, Python, js.
sh ./setup/go_packages.sh
sh ./setup/js_packages.sh
sh ./setup/python_packages.sh
