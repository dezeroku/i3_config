#!/bin/bash
# Install Vundle (VIM plugins manager)
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# .vimrc should be already linked, because link_dotfiles.sh was run before

# Install all plugins mentioned in .vimrc.
vim -c "PluginInstall"

# Compile necessary YCM files.
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer --go-completer --js-completer --java-completer
cd -
