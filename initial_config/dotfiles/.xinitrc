setxkbmap pl
#exec i3 #changed for python resolution dependent config
python3 ~/.config/i3/scripts/resolution.py run_i3
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources
