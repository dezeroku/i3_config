#!/usr/bin/bash
#Arch install base base-devel
#that script
#reboot
#VOILA

./pacaur_install.sh
./all_programs_used.sh
#set new mime types, for freshly install programs
./configure.sh

#copy urxvt settings
cp ~/.config/i3/initial_config/files/.Xdefaults ~/
cp ./.config/i3/initial_config/files/.xinitrc ~/

#copy sublime config (TO DO IN FUTURE)

