#!/bin/bash

# TODO: rewrite with path checking in python.

mkdir ~/backup_dotfiles
mkdir ~/.config
mv ~/.vimrc ~/backup_dotfiles
mv ~/.xinitrc ~/backup_dotfiles
mv ~/.Xdefaults ~/backup_dotfiles
mv ~/.config/ranger/rc.conf ~/backup_dotfiles
mv ~/.tmux.conf ~/backup_dotfiles
mv ~/.config/dunst/dunstrc ~/backup_dotfiles
mv ~/.config/rofi/config ~/backup_dotfiles
mv ~/.config/qutebrowser/config.py ~/backup_dotfiles

mkdir ~/.config/dunst
mkdir ~/.config/rofi
mkdir ~/.config/qutebrowser

echo "Your original files are backed up in ~/backup_dotfiles folder."

mkdir ~/.config/ranger
ln -f ~/.config/i3/initial_config/dotfiles/rc.conf ~/.config/ranger/rc.conf
ln -f ~/.config/i3/initial_config/dotfiles/.vimrc ~/.vimrc 
ln -f ~/.config/i3/initial_config/dotfiles/.Xresources ~/.Xresources
# Don't symlink .xinitrc cause it may vary much between devices
#ln -f ~/.config/i3/initial_config/dotfiles/.xinitrc ~/.xinitrc 
ln -f ~/.config/i3/initial_config/dotfiles/.tmux.conf ~/.tmux.conf
ln -f ~/.config/i3/initial_config/dotfiles/dunstrc ~/.config/dunst/dunstrc
ln -f ~/.config/i3/initial_config/dotfiles/rofi_config ~/.config/rofi/config
ln -f ~/.config/i3/initial_config/dotfiles/qute_config.py ~/.config/qutebrowser/config.py
