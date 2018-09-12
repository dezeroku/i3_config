#!/bin/sh

# That is the file that should be run when you want to set up your shiny new Arch Linux install.
# It takes care of installing python, setting up some repos and calls python installer in the end.

# Enable multilib pacman.
echo '[multilib]' | sudo tee --append /etc/pacman.conf
echo 'Include = /etc/pacman.d/mirrorlist' | sudo tee --append /etc/pacman.conf

# Find fastest servers and use them with pacman.
sudo pacman -Sy pacman-contrib
rankmirrors -n 15 /etc/pacman.d/mirrorlist > mirrorlist
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist_backup
sudo mv mirrorlist /etc/pacman.d/mirrorlist

# Run system upgrade.
sudo pacman -Syu

# Install python3 so we can run setup.py (isn't it already installed?)
sudo pacman -S python3

# Let the python do the hard work.
python3 setup.py
