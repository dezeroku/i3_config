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

### Directory tree

+ configs
 1 1280x800 -> Configuration files to use when resolution equals 1280x800
 2 1920x1080 -> Configuration files to use when resolutin equals 1920x1080
 3 base -> Configuration files that are base on which resolution-specific configs can build. Also contains config\_fallback which is merged when no resolution is matched
+ scripts -> Contains all logic of repository
 1 i3
  * next\_workspace.py -> Changes to next active i3 workspace when called.
 2 setup.py -> Used to manage installation, install programs, configure mime, link dotfiles etc.
 3 resolution.py -> Merging i3 configurations, locking screen etc.
 4 hibernate -> turns off qutebrowser and hibernates computer, to be run from commandline
+ setup
 1 dotfiles -> Configuration files for programs mentioned above
 2 shell'_files -> Files that will be sourced to shell
 3 apps_list -> Lists of applications to be installed.
+ README.MD

### Installation
You should clone that repo, open scripts folder and run install.sh script. It should take care of everything.

After it finished you should add absolute path to resolution.py to your .xinitrc and call it to run i3.

It should look similar to this:

`/home/d0ku/i3_config/scripts/resolution.py run --start-i3`

That't the most basic way to go.

Of course you will have to decide what apps you want to install, press some Y's on pacman run etc. but most of the job should be done by the program itself. If you want to change defaults you should mess up with configuration files in /setup and /configs

### Usage
The easiest option to not mess up with paths is to add absolute path to resolution.py to your .xinitrc file, add scripts folder to PATH variable and whenever you want to run the app just call resolution.py from terminal.

### Credits
- wallpaper\_0.png, lock\_0.png - [Damian Lickindorf](https://www.instagram.com/lickindorf_fotografia/)
- lock\_1.png -  Photo by [Markus Spiske](https://unsplash.com/@markusspiske) on Unsplash
- Tmux config is very much based on work of [@gpakosz](https://github.com/gpakosz/). I recommend visiting repo with his [config for tmux ](https://github.com/gpakosz/.tmux).
