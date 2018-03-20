#!/usr/bin/bash
#Arch install base base-devel
#that script
#reboot
#VOILA

./pacaur_install.sh
sudo pacman -Syu
sudo pacman -S - < arch_repo_apps.txt
pacaur -S - < arch_aur_apps.txt
#./install_programs_arch.sh
#set new mime types, for new programs
./configure_mime_arch.sh

#copy urxvt settings
cp ~/.config/i3/initial_config/files/.Xdefaults ~/
#copy Xorg startx settings
cp ~/.config/i3/initial_config/files/.xinitrc ~/

#copy sublime config (TODO IN FUTURE)

