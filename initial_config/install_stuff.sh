#!/usr/bin/bash
#Arch install base base-devel
#that script
#reboot
#VOILA

sudo ./pacaur_install.sh
./all_programs_used.sh
#set new mime types, for freshly install programs
./configure.sh

#copy urxvt settings
cp ./files/.Xdefaults ~/

#copy sublime config (TO DO IN FUTURE)

