#/bin/sh
# Installs all apps and sets all settings.

# Install AUR manager.
#./yay_install.sh

# Add sublime text repository.
curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg

#echo -e "\n[sublime-text]\nServer = https://download.sublimetext.com/arch/stable/x86_64" | sudo tee -a /etc/pacman.conf

# Install all official repos apps.
sudo pacman -Syu $(echo $(cat arch_repo_apps.txt))

# Install apps from AUR.
yay -S $(echo $(cat arch_aur_apps.txt))

# Make npm runnable without sudo, and store it config in home directory.
mkdir ~/npm_global

npm config set prefix '~/npm_global'

echo "export PATH=~/npm_global/bin:$PATH" >> ~/.bashrc

# Link important configs (existing files are moved to backup folder).
./link_dotfiles.sh

# Set correct mime types for programs (default programs).
./configure_mime_arch.sh

# Configure VIM.
./configure_vim.sh

# Configure tmux.
./configure_tmux.sh

# Install go, python and js packages
./go_packages.sh
./python_packages.sh
./js_packages.sh

# Configure thefuck (copy alias).
fuck
fuck

#copy sublime config (TODO IN FUTURE)
echo FINISHED
