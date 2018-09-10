#This file is responsible for loading specific files for each resolution, It was created to easy maintain two layouts, one for laptop (1280x800), and one for PC (1920x1080), but it was made to work with other resolutions also
#Config base file now serves as a fallback config
import subprocess
import argparse
import sys
import os
from pathlib import Path

def get_resolution():
    command = "xrandr  | grep \* | cut -d' ' -f4"
    result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    for line in result.stdout.readlines():  # read and store result in log file
        pass
        #print(line)

    temp = line.decode("utf-8")

    resolution = ""
    for x in temp:
        if x != "\n":
            resolution += x

    if resolution is None:
        print("Could not get resolution!")
        sys.exit(1)
    return resolution

def file_exists(path):
    pass

def convertToNumber(number):
    try:
        number = int(number)
    except: #TODO: specify exception
        print("Could not convert to a number: "+number)
        sys.exit(2)
    return number

class Locker:
    """All methods arguments should be already parsed ints."""
    default_color = "#cccccc"

    def __init__(self, lock_images_path):
        self.lock_images_path = lock_images_path
        pass

    def lock_now(self,image_number=-1):
        final_path = self.lock_images_path+str(image_number)+"_lock.png"
        print(final_path)
        if (image_number!=-1 and
            os.path.exists(final_path)):
            os.system("i3lock -c 000000 -i " + final_path)
        else:
            os.system("i3lock -c 000000")

        # Turn screen off.
        os.system("xset dpms force standby")

    def enable_lock_daemon(self,image_number=-1):
        if (image_number!=-1 and
            os.path.exists(self.lock_images_path + str(image_number) +
                           "_lock.png")):
            os.system("xss-lock -- i3lock -c 000000 -i " +
                      self.lock_images_path +
                      str(lock_number)+"_lock.png" + " &")
        else:
            os.system("xss-lock -- i3lock -c 000000" + " &")

class Runner:
    pass

class Wallpaper:
    pass

def get_parser_locker(parser):
    home_directory=str(Path.home())
    locking = parser.add_mutually_exclusive_group()
    locking.add_argument("--lock-screen",
                        help="Locks screen and blanks display.",
                        action="store_true")
    locking.add_argument("--set-up-locker", help="Start process in \
                        background which checks whether screen has to be \
                        locked due to inactivity or system suspend.",
                        action="store_true")

    parser.add_argument("--lock-images-path", help="Point to directory\
                        which contains correctly descripted images to use with\
                        lockscreen. (absolute path)",
                        default=home_directory + "/.config/i3/configs/" +
                        get_resolution() +
                        "/wallpapers/")

    parser.add_argument("--lock-image-number", help="Number of image\
                        that should be used as a lockscreen wallpaper. Number\
                        must be compliant with naming standards.", type=int,
                        default=0)

def get_parser_runner(parser):
    home_directory=str(Path.home())
    exclusive = parser.add_mutually_exclusive_group()

    exclusive.add_argument("--start-i3", help="Starts i3wm with \
                           provided parameters.",action="store_true")
    exclusive.add_argument("--reload-i3-config", help="Recreates the\
                           config file and forces i3 refresh to use it.",
                           action="store_true")
    exclusive.add_argument("--start-py3status", help="Starts status bar\
                           manager.", action="store_true")

    parser.add_argument("--config-base-path", help="Path where base config\
                           file is located. (absolute path)",
                           default=home_directory + "/.config/i3/configs/base/")


def set_up_parsers():
    parser = argparse.ArgumentParser("Main manager for system.")

    parser_getter = parser.add_subparsers()

    parser_runner = parser_getter.add_parser("run", help='Handle starting i3\
                                            functionality')
    get_parser_runner(parser_runner)
    parser_runner.set_defaults(func=runner)

    parser_locker = parser_getter.add_parser("lock", help='Handle lock functionality')
    get_parser_locker(parser_locker)
    parser_locker.set_defaults(func=locker)

    return parser

def runner(args):
    pass

def locker(args):
    locker = Locker(args.lock_images_path)
    image_number = args.lock_image_number

    if args.lock_screen:
        locker.lock_now(image_number)
    elif args.set_up_locker:
        locker.enable_lock_daemon(image_number)


def main():
    parser = set_up_parsers()

    args = parser.parse_args()
    args.func(args)
        # Do something with groups in argparse, so it's logical.



if __name__ == "__main__":
    main()

sys.exit(0)
lock_number=0;
wallpaper_number=0;
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

if sys.argv[1] == "lock_screen_and_suspend":
    if len(sys.argv)>2:
        if os.path.exists(path+str(sys.argv[2])+"_lock.png"):
            lock_number=int(sys.argv[2])
        else:
            print("FALLBACK")

    os.system("i3lock -c 000000 -i " + path +str(lock_number)+
              "_lock.png" + " && systemctl suspend")


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
