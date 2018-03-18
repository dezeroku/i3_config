#This file is responsible for loading specific files for each resolution, It was created to easy maintain two layouts, one for laptop (1280x800), and one for PC (1920x1080), but it was made to work with other resolutions also
#Config base file now serves as a fallback config
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
current_config_path=home_directory+"/.config/i3/configs/current/config"
config_base_path=home_directory+"/.config/i3/configs/base/config"
config_fallback_path=home_directory+"/.config/i3/configs/base/config_fallback"
current_folder_path=home_directory+"/.config/i3/configs/current/"
fallback_status_path=home_directory+"/.config/i3/configs/base/i3status.conf"

#path += resolution + "/"  # e.g ~/.config/i3/wallpapers/1280x800/
config_path += resolution +"/"+"config" # e.g ~/.config/i3/configs/1280x800/
status_path+= resolution +"/"+"i3status.conf" #e.g ~/.confid/i3/configs/1920x1080/i3status.conf

if sys.argv[1] == "set_lock_screen" :
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            lock_number=-1
            print("FALLBACK")
    if lock_number!=-1:
        os.system("xss-lock -- i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png" + " &")
    else:
        os.system("xss-lock -- i3lock -c 000000" + " &")

if sys.argv[1] == "lock_screen":
    #TODO: running only "xset dpms force standby" locks the screen itself, check behaviour

    #however running first "xset s activate" is probably better practice

    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            lock_number=-1
            print("FALLBACK")
    
    if lock_number!=-1:
        os.system("i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png")
    else:
        os.system("i3lock -c 000000")

    os.system("xset dpms force standby") #blanks screen
    #os.system("xset s off -dpms ") #this prevents screen from going black

if sys.argv[1]== "lock_screen__stay_on":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("i3lock -c 000000 -i " + path + str(lock_number)+"_lock.png")

if sys.argv[1] == "reload_config":
    if os.path.exists(config_path)==True:
        if not os.path.exists(current_folder_path):
            os.system("mkdir "+current_folder_path)
        with open(current_config_path,"w") as current_config:
            current_config.write("#DO NOT EDIT THIS FILE, IT IS AUTOMATICALLY GENERATED BY SCRIPT \n")
            current_config.write("#IF YOU WANT TO CHANGE CONFIG, DO IT IN RESOLUTION SPECIFIC OR BASE FOLDER \n")
            current_config.write("\n\n\n")
            with open(config_base_path,"r") as base_config:
                current_config.write("#BASE CONFIG PART\n")
                current_config.write(base_config.read())
                current_config.write("\n\n\n")

            with open(config_path,"r") as specific_config:
                current_config.write("#RESOLUTION SPECIFIC PART \n")
                current_config.write(specific_config.read())
                current_config.write("\n")

        print("Config exists, now reload your config")
    else:
        with open(current_config_path,"w") as current_config:
            current_config.write("#FALLBACK CONFIG USED, NO SUPPORTED RESOLUTION FOUND \n")
            current_config.write("#DO NOT EDIT THIS FILE, IT IS AUTOMATICALLY GENERATED BY SCRIPT \n")
            current_config.write("#IF YOU WANT TO CHANGE CONFIG, DO IT IN RESOLUTION SPECIFIC OR BASE FOLDER \n")
            current_config.write("\n\n\n")
            with open(config_base_path,"r") as base_config:
                current_config.write("#BASE CONFIG PART\n")
                current_config.write(base_config.read())
                current_config.write("\n\n\n")

            with open(config_fallback_path,"r") as specific_config:
                current_config.write("#FALLBACK CONFIG USED \n")
                current_config.write(specific_config.read())
                current_config.write("\n")

        print("Fallback, now reload your config")
  

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
        if not os.path.exists(current_folder_path):
            os.system("mkdir "+current_folder_path)
        with open(current_config_path,"w") as current_config:
            current_config.write("#DO NOT EDIT THIS FILE, IT IS AUTOMATICALLY GENERATED BY SCRIPT \n")
            current_config.write("#IF YOU WANT TO CHANGE CONFIG, DO IT IN RESOLUTION SPECIFIC OR BASE FOLDER \n")
            current_config.write("\n\n\n")
            with open(config_base_path,"r") as base_config:
                current_config.write("#BASE CONFIG PART\n")
                current_config.write(base_config.read())
                current_config.write("\n\n\n")

            with open(config_path,"r") as specific_config:
                current_config.write("#RESOLUTION SPECIFIC PART \n")
                current_config.write(specific_config.read())
                current_config.write("\n")

        os.system("i3 -c "+current_config_path)
        print("Config exists")
    else:
        with open(current_config_path,"w") as current_config:
            current_config.write("#FALLBACK CONFIG USED, NO SUPPORTED RESOLUTION FOUND \n")
            current_config.write("#DO NOT EDIT THIS FILE, IT IS AUTOMATICALLY GENERATED BY SCRIPT \n")
            current_config.write("#IF YOU WANT TO CHANGE CONFIG, DO IT IN RESOLUTION SPECIFIC OR BASE FOLDER \n")
            current_config.write("\n\n\n")
            with open(config_base_path,"r") as base_config:
                current_config.write("#BASE CONFIG PART\n")
                current_config.write(base_config.read())
                current_config.write("\n\n\n")

            with open(config_fallback_path,"r") as specific_config:
                current_config.write("#FALLBACK CONFIG USED \n")
                current_config.write(specific_config.read())
                current_config.write("\n")

        os.system("i3 -c "+current_config_path)
        print("Fallback")

if sys.argv[1]=="py3status":
    if os.path.exists(status_path)==True:
        os.system("py3status -c "+status_path)
        print("Config exists")
    else:
        os.system("py3status -c "+fallback_status_path)
        print("Fallback")
