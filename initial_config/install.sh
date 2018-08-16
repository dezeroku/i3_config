#!/bin/sh

# Enable multilib pacman.
echo '[multilib]' | sudo tee --append /etc/pacman.conf
echo 'Include = /etc/pacman.d/mirrorlist' | sudo tee --append /etc/pacman.conf

# Find fastest servers and use them with pacman.
sudo pacman -S pacman-contrib
rankmirrors -n 15 /etc/pacman.d/mirrorlist > mirrorlist
sudo mv /etc/pacman.d/mirrorlist /etc/pacman.d/mirrorlist_backup
sudo mv mirrorlist /etc/pacman.d/mirrorlist
rm mirrorlist

# Run system upgrade.
sudo pacman -Syu

# Install python so we can run install.py
sudo pacman -S python3

# Ask whether detailed or normal installation.
echo "Available installation types:"
echo "   [1] Automated"
echo "   [2] Detailed (work in progress)"
echo "Choose number of your installation type:"

read installation_type

if [ "$installation_type" = "1" ]; then
    ./install_auto.sh
elif [ "$installation_type" = "2" ]; then
    python3 install.py
else 
    echo "Incorrect option. Exiting..."
fi
