#!/bin/bash
#Arch install base base-devel
#that script
#reboot
#VOILA

./install_program_gentoo.sh
#set new mime types, for freshly install programs
./configure_mime_gentoo.sh

#copy urxvt settings
cp ~/.config/i3/initial_config/files/.Xdefaults ~/
#copy Xorg startx settings
cp ~/.config/i3/initial_config/files/.xinitrc ~/

#copy sublime config (TODO IN FUTURE)

