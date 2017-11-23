#!/usr/bin/bash
#Arch install base base-devel
#that script
#reboot
#VOILA

sudo ./pacaur_install
./all_programs_used.sh
#set new mime types, for freshly install programs
./file_mime_bindings.sh

#copy urxvt settings
cp ./.Xdefaults ~/

#copy sublime config (TO DO IN FUTURE)

