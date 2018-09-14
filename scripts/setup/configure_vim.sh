#!/bin/bash
# Install Vundle (VIM plugins manager)
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# Update if already installed.
git pull ~/.vim/bundle/Vundle.vim

# Install all plugins mentioned in .vimrc.
vim -c "PluginInstall" -c "q" -c "q"

# Compile necessary YCM files.
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer --go-completer --js-completer --java-completer
cd -
# Install binaries for vim-go (debugging and stuff)
vim -c "GoInstallBinaries" -c "q"
