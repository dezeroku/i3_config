#!/bin/sh

# This script should be run when you are already chrooted into Arch Linux and just want to set up everything.

# Move files to the place they should be in.

mkdir ~/.config
mkdir ~/.config/i3
mv ../../i3_config/* ~/.config/i3/ -r
cd ~/.config/i3

# Set up pacman source files.

username=$(whoami)

su -c "pacman -Sy;
       pacman -S sudo;
       usermod -aG sudo whoami;"

echo "Now relog and run install.sh"
