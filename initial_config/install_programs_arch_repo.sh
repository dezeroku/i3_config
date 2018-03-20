#!/usr/bin/bash


#pre install
#sublime_text (needs new repo)
    
#curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
#echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf



#INSTALL
#
#xorg
sudo pacman -S  xorg xorg-xinit \
#i3 base
#i3
i3 \
#audio
alsa-utils pulseaudio pavucontrol pulseaudio-bluetooth pulseaudio-equalizer pulseaudio-jack \
#i3 specific stuff
#playerctl #music control
#dmenu #menu support
#ponymix #volume changes
#feh #only if you want ot use wallpapers
#nvidia-smi #if you want to display nvidia graphic card temperature
#pygame #install it using pip, it enables sounds in UI
playerctl dmenu ponymix feh \
#web
#firefox
firefox \
# audio, video
#qt4 #(GUI fo VLC)
#qmmp
#vlc
vlc qt4 qmmp \
# images
#sxiv
#gimp
gimp sxiv \
# archives
#xarchiver
#p7zip
p7zip xarchiver \
# file managers
#pcmanfm
#ranger #(mc?)
ranger pcmanfm \
# documents, text editing, pdf
#libreoffice
#vim
#zathura (lightweight and highly customizable document viewer)
#zathura-pdf-mupdf (plugin for pdf)
vim libreoffice zathura zathura-pdf-mupdf \
sublime-text \
#alternative way
#pacaur -S --noconfirm sublime-text-dev
#finding disk usage
ncdu \
#latex, latex languages
texlive-most texlive-lang \
wine winetricks \
qemu qemu-arch-extra \
# fonts
#ttf-hack
ttf-hack \
# terminals
#terminator
#rxvt-unicode #(urxvt)
terminator rxvt-unicode \
# IDE
#eclipse #(optional)
eclipse \
# torrents
#deluge #(optional)
deluge \
# languages and stuff
#python3
#python
#ruby
#jdk9-openjdk #(java 9 jdk)
#docker (i find it useful quite often) (it is NOT enabled by default, you need to 
#sudo systemctl start docker
#sudo systemctl enable docker
# if you want to have it enabled)
python3 ruby jdk9-openjdk docker \
#ntfs non root permissions
ntfs-3g fuse \
#notifications
dunst \
#redshift
redshift \ 
# network config
networkmanager \
#network manager applet
network-manager-applet \
#post install

#sudo usermod -aG docker $USER 