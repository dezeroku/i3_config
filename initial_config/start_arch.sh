#!/bin/bash

# Install Arch Linux (pacstrap base base-devel)
# You have to add yourself to sudo (currently working on changing that).
# Run that script. IMPORTANT: This script should be done as normal user, not root! Also the user pwd should be this folder.
# Also this script requires user input (e.g. accepting pacman installations).
# Reboot.
# Your computer should be configured now.

# Install AUR manager.
./pacaur_install.sh

# Add sublime text repository.
curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg

echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf

# Enable multilib pacman.
echo '[multilib]' | sudo tee --append /etc/pacman.conf
echo 'Include = /etc/pacman.d/mirrorlist' | sudo tee --append /etc/pacman.conf

# Run system upgrade.
sudo pacman -Syu

# Find fastest servers and use them with pacman.
rankmirrors -n 15 /etc/pacman.d/mirrorlist > mirrorlist
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist_backup
sudo mv mirrorlist /etc/pacman.d/mirrorlist
rm mirrorlist

# Run system upgrade.
sudo pacman -Syu

# Install all official repos apps. TODO: ERROR WITH - mark
sudo pacman -S $(echo $(cat arch_repo_apps.txt))

# Install apps from AUR.
pacaur -S $(echo $(cat arch_aur_apps.txt))

# Set correct mime types for programs (default programs).
./configure_mime_arch.sh

# Link important configs (overrides existing files by default).
./link_dotfiles.sh

# Configure VIM.
./configure_vim.sh

# Configure thefuck (copy alias).
fuck
fuck

#copy sublime config (TODO IN FUTURE)
echo FINISHED
