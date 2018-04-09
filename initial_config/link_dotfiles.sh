#!/bin/bash

mkdir ~/backup_dotfiles
mv ~/.vimrc ~/backup_dotfiles
mv ~/.xinitrc ~/backup_dotfiles
mv ~/.Xdefaults ~/backup_dotfiles

echo "Your original files are backed up in ~/backup_dotfiles folder."

ln -f ~/.config/i3/initial_config/dotfiles/.vimrc ~/.vimrc 
ln -f ~/.config/i3/initial_config/dotfiles/.Xdefaults ~/.Xdefaults 
ln -f ~/.config/i3/initial_config/dotfiles/.xinitrc ~/.xinitrc 
