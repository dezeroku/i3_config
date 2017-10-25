import sys,os
from pathlib import Path
#ADD BETTER TOGGLE SUPPORT
#touchpad toggle is now python only code

touchpad_name="\'ETPS/2 Elantech Touchpad\'" #write you touchpad device identifier in that field, remember to edit ./touchpad_toggle also
home_directory=str(Path.home())
path=home_directory+"/.config/i3/scripts/"

if len(sys.argv)<2:
    print("See help") # you should write that help by the way xD
    #exit program

if sys.argv[1]=="turn_on":
    os.system("xinput enable "+touchpad_name)

if sys.argv[1]=="turn_off":
    os.system("xinput disable "+touchpad_name)

state=False

if len(sys.argv)==0 or sys.argv[1]=="toggle":
    with open(path+"state.txt","r") as state_file:
        if state_file.read()=="enabled":
            state=True
    if state==True:
        os.system("xinput disable "+touchpad_name)
        with open(path+"state.txt","w") as state_file:
            state_file.write("disabled")
    if state==False:
        os.system("xinput enable "+touchpad_name)
        with open(path+"state.txt","w") as state_file:
            state_file.write("enabled")
    #os.system("sh ~/.config/i3/scripts/touchpad_toggle")
