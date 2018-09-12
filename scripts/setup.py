"""Initial installation and setup of my Arch Linux config.
Should handle installing packages and linking up some dotfiles.

Steps:
    Install AUR helper (yay currently)
    Install stuff
    Install AUR stuff
    Some setup for npm
    Link dotfiles
    Install language packages (go, python, js etc.)
    Configure MIME and let apps update their plugins or whatever
    Configure thefuck
    add required shell sources
    Enable vnstat
By d0ku 2018"""

import os
# We are going to use it for linking.
from base import get_root_folder

def install_yay():
    """Installs yay AUR helper."""
    os.system("git clone https://aur.archlinux.org/yay.git;\
              cd yay;\
              makepkg -si;\
              cd ..;\
              rm -rf yay;")

def main():
    """Function which is called, when script is executed directly and not used
    as a library."""
    install_yay()
    pass

if __name__ == "__main__":
    main()
