#!/usr/bin/bash
#update pacman sources
sudo pacman -Sy

#upgrade system (optional, but recommended)
sudo pacman -Syu

# network config
sudo pacman -S networkamanager

#install pacaur (optional, but recommended, it is just faster to install packages from AUR), enabled in install_stuff by default
#sudo ./pacaur_install

#i3 base
#i3
sudo pacman -S i3

#i3 specific stuff
#playerctl #music control
#dmenu #menu support
#pamixer #volume changes
#xss-lock-git # for lid close and screen timeout support (non-git version has cpu problems)
#ttf-font-icons #workspace icons
#py3status #better i3status
#feh #only if you want ot use wallpapers
#nvidia-smi #if you want to display nvidia graphic card temperature
#pygame #install it using pip, it enables sounds in UI
sudo pacman -S playerctl dmenu pamixer py3status feh 
sudo pip3 install pygame
pacaur -S xss-lock-git ttf-font-icons 

#web
#vimb 
#firefox
sudo pacman -S firefox vimb
# audio, video
#qt4 #(GUI fo VLC)
#deadbeef
#vlc
sudo pacman -S vlc deadbeef qt4
# images
#sxiv
#gimp
sudo pacman -S gimp sxiv
# archives
#xarchiver
#p7zip
sudo pacman -S p7zip xarchiver
# file managers
#pcmanfm
#ranger #(mc?)
sudo pacman -S ranger pcmanfm
# documents, text editing, pdf
#evince
#libreoffice
#vim
#zathura (lightweight and highly customizable document viewer)
#zathura-pdf-mupdf (plugin for pdf)
sudo pacman -S vim evince libreoffice zathura zathura-pdf-mupdf
#sublime_text (needs new repo)
    
#curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
#echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf
#sudo pacman -Syu sublime-text
#alternative way
pacaur -S sublime-text
# windows files support (optional), virtualbox
#wine 
#winetricks
#virtualbox
sudo pacman -S wine winetricks virtualbox
# fonts
#ttf-hack
sudo pacman -S ttf-hack
# terminals
#terminator
#rxvt-unicode #(urxvt)
sudo pacman -S terminator rxvt-unicode
# IDE
#eclipse #(optional)
sudo pacman -S eclipse
# torrents
#deluge #(optional)
sudo pacman -S deluge
# languages and stuff
#python3
#python
#ruby
#jdk9-openjdk #(java 9 jdk)
#docker (i find it useful quite often) (it is NOT enabled by default, you need to 
#sudo systemctl start docker
#sudo systemctl enable docker
# if you want to have it enabled)
sudo pacman -S python3 ruby jdk9-openjdk docker
sudo usermod -aG docker $USER

#ntfs non root permissions
sudo pacman -S ntfs-3g fuse
