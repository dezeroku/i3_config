## About
That repository contains scripts and files that I use to set up new Arch Linux installs.

It contains:

+ i3 config files (base and resolution specific)
+ 'dotfiles' for:
  1. tmux
  2. vim
  3. ranger
  4. qutebrowser
  5. URxvt (.Xresources)
  6. dunst
  7. rofi
+ 2 lockscreen wallpapers
+ 1 desktop wallpaper

### Installation
There is an 'install\_auto.sh' script in 'initial\_config' folder and I use it to set everything up.

Refactoring it and automating installation process even more is one of the top priorities TODOs.

If you do not want to install all the stuff I do, you should read resolution.py script in 'scripts' folder and change configs/base and configs/{resolution} to suit your needs.

### Credits
- wallpaper\_0.png, lock\_0.png - [Damian Lickindorf](https://www.instagram.com/lickindorf_fotografia/)
- lock\_1.png -  Photo by [Markus Spiske](https://unsplash.com/@markusspiske) on Unsplash
- Tmux config is very much based on work of [@gpakosz](https://github.com/gpakosz/). I recommend visiting repo with his [config for tmux ](https://github.com/gpakosz/.tmux).
