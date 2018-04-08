#!/usr/bin/bash

# Install Arch Linux (base base-devel)
# Run that script.
# Reboot.
# Your computer should be configured now.

# Install AUR manager.
./pacaur_install.sh

# Run system update.
sudo pacman -Syu

# Install all official repos apps.
sudo pacman -S - < arch_repo_apps.txt

# Install apps from AUR.
pacaur -S - < arch_aur_apps.txt

# Set correct mime types for programs (default programs).
./configure_mime_arch.sh

# Link important configs.
./link_dotfiles.sh

# Configure VIM.
./configure_vim.sh

# Configure thefuck (copy alias).
fuck
fuck

#copy sublime config (TODO IN FUTURE)
echo FINISHED
