#Install Vundle and link vim config??? TODO:
git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

#TODO: run PluginInstall in vim

#link file or something

vim -c "PluginInstall"
# Paths can be different?
cd ~/.vim/bundle/YouCompleteMe
./install.py --clang-completer --go-completer --js-completer --java-completer
