#This file is responsible for loading specific files for each resolution, It was created to easy maintain two layouts, one for laptop (1280x800), and one for PC (1920x1080), but it was made to work with other resolutions also
import subprocess
import sys
import os
from pathlib import Path
command = "xrandr  | grep \* | cut -d' ' -f4"

result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
for line in result.stdout.readlines():  # read and store result in log file
    print(line)

temp = line.decode("utf-8")

resolution = ""
for x in temp:
    if x != "\n":
        resolution += x

print(resolution)

lock_number=0;
wallpaper_number=0;
home_directory=str(Path.home()) #this is potentially dangerous
path = home_directory+"/.config/i3/configs/"+resolution+"/wallpapers/" # e.g ~/.config/i3/configs/1280x800/wallpapers/
config_path=home_directory+"/.config/i3/configs/"
status_path=home_directory+"/.config/i3/configs/"

fallback_status_path=home_directory+"/.config/i3/default/i3status.conf"
fallback_config_path=home_directory+"/.config/i3/default/config"

#path += resolution + "/"  # e.g ~/.config/i3/wallpapers/1280x800/
config_path += resolution +"/"+"config" # e.g ~/.config/i3/configs/1280x800/
status_path+= resolution +"/"+"i3status.conf" #e.g ~/.confid/i3/configs/1920x1080/i3status.conf

if sys.argv[1] == "set_lock_screen" :
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("xss-lock -- i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png" + " &")

if sys.argv[1] == "lock_screen":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png")
    os.system("xset dpms force standby") #blanks screen
    os.system("xset s off -dpms ") #this prevents screen from going black

if sys.argv[1]== "lock_screen__stay_on":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png")

if sys.argv[1] == "set_wallpaper":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_wallpaper.png"):
            wallpaper_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("feh --bg-scale "+path+str(wallpaper_number)+"_wallpaper.png")

if sys.argv[1] == "lock_screen_and_suspend":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("i3lock -c 000000 -i " + path +str(lock_number)+
              "_lock.png" + " && systemctl suspend")

if sys.argv[1]=="run_i3":
    if os.path.exists(config_path)==True:
        os.system("i3 -c "+config_path)
        print("Config exists")
    else:
        os.system("i3 -c "+fallback_config_path)
        print("Fallback")

if sys.argv[1]=="py3status":
    if os.path.exists(status_path)==True:
        os.system("py3status -c "+status_path)
        print("Config exists")
    else:
        os.system("py3status -c "+fallback_status_path)
        print("Fallback")
