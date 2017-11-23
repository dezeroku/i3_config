This is my customized i3 environment with some additional scripts and changes.
It is quite easy to notice that it was done on Arch Linux (all the AUR packages), I don't know whether this packages are available on other distributions, but I strongly recommend to try Arch ;)

Main concept standing behind those files is to made independent config for resolutions (well, it was made on a 1920x1080 PC and 1280x800 laptop), which are kind of ID for device (I know it is weak ;).

For that concept to work you should add this "python3 ~/.config/i3/scripts/resolution.py run_i3" to your .xinit line or replace your i3 starting routine with that line.

For brightness keys to work with my script , you should add NOPASSWD entry in /etc/sudoers to work properly (you have to give NOPASSWD sudo access to change_brightness file)

By default all files should be stored in ~/.config/i3/ , otherwise it won't work.

i3status.conf i3 config and some more files are stored in ~/.config/i3/configs/your_resolution/ and should be edited there

INFO: 

All of this scripts are written by myself, and for myself, therefore some of them probably won't work for you, feel free to edit them to your needs. I plan to release Docs in near future.



TODO:

 create one main file, and connect it with resolution ones -> DONE

 add screenshot sound


Now, full config consists of a base and resolution specific one.


First, for full functionality you need to install:

playerctl (for music control)

dmenu (menu start app for i3)

pamixer (for volume changes)

xss-lock-git ( normal version has CPU problems, available in AUR) 

ttf-font-icons (pretty workspace icons, available in AUR) 

python3 (well, you really SHOULD have it installed)  

py3status (better i3status, available in AUR)

feh (only if you want to use wallpapers)

nvidia-smi (nvidia graphics temperature only)

pygame (python3 library, install it using pip, for all kind of sounds played in UI)
