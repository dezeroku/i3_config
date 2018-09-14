#!/bin/sh

# That is the file that should be run when you want to set up your shiny new Arch Linux install.
# NOTICE: At this point you should be booted into Arch Linux directly, and have sudo set up and working.
# It takes care of installing python, setting up some repos and calls python installer in the end.
# It is best to have installed at least base and base-devel.



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

# Install python3 and git so we can run setup.py (isn't python3 already installed?)
sudo pacman -S python3 git

# Let the python do the hard work.

# Install yay.
python3 setup.py install --install-aur-helper yay
# Install official repo packages. (We run it with sudo to get necessary privileges for pacman.)
sudo python3 setup.py install --install-from-file ./apps_list/arch_repo_apps --install-command S --do-not-reinstall
# Install AUR packages.
python3 setup.py install --install-from-file ./apps_list/arch_aur_apps --install-command S --package-manager yay --do-not-reinstall
