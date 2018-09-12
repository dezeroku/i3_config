"""Initial installation and setup of my Arch Linux config.
Should handle installing packages and linking up some dotfiles.

Steps:
    Install AUR helper (yay currently) Ok
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

import subprocess
import re
import sys

# We are going to use it for linking.
from base import get_root_folder

class IncorrectAppsListError(BaseException):
    """Thrown when there was error in parsing apps list."""
    pass

def get_user_input_install():
    """Display install dialog."""
    # That loop will surely end, so it's safe to use here.
    while True:
        temp = input("Do you want to install? [Y]/n")
        if temp in ("", "Y", "y"):
            return True
        if temp in ("n", "N"):
            return False

class AppsGroup:
    """Displays apps to user and checks whether he wants it to be installed or
    not."""
    applications = []
    accepted = []

    def __init__(self, name):
        self.name = name

    def add_application(self, app_name):
        """Adds application to list of apps that should be displayed to
        user."""
        self.applications.append(app_name)

    def process_one(self):
        """Displays to user whether he wants to install first of the not yet
        listed apps. It moves it to accepted if user accepts or deletes that
        app from queue. Returns False when queue is empty, True otherwise."""
        if not self.applications:
            return False
        app = self.applications.pop()

        print("App name: "+app.name)
        if app.description:
            print(app.description)

        print("\n")
        install = get_user_input_install()
        if install:
            self.accepted.append(app)

        return True

    def process_all(self):
        """Processes all apps in group, using self.process_one."""
        while self.process_one():
            pass
        print("All apps from group processed.")
        if self.accepted:
            print("To be installed: ")
            for app in self.accepted:
                print(app + " ")
            return True

        print("Nothing to be installed.")
        return False

class App:
    """Contains info about one application from list."""
    def __init__(self, name, description=False):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

def install_yay():
    """Installs yay AUR helper."""
    subprocess.call(["sh", "setup/install_yay.sh"])

def parse_apps_list(file_name):
    """That function returns groups of applications to install (AppsGroup).
    All files that go through this function should be correctly prepared:
    $$ tags start a group and name of a group should be between them.
    ?? tags end group of apps
    ** tags are a description of app functionality
    There should be one app/group tag per line.
    Lines starting with '#' are ignored.
    If line contains a group name, it must end immediately after $$ (no
    whitespaces allowed).
    All description must fit in one line.
    Same goes for ** and ??
    Example:
        $$GUI$$
        xorg
        i3 **window manager**
        ??
    defines a group of apps called GUI, that consists of xorg and i3 to be
    installed. i3 also has description 'window manager'"""
    stack = []
    groups = []

    group_start_str = "\$\$.*\$\$$"
    group_end_str = "^\?\?$"
    description_str = "\*\*.*\*\*$"
    just_app_name_str = "^[^\$\*\?\\n\ ]*"

    group_start = re.compile(group_start_str)
    group_end = re.compile(group_end_str)
    description = re.compile(description_str)
    just_app_name = re.compile(just_app_name_str)

    with open(file_name, "r") as app_list:
        curr_group = None
        counter = 0
        for line in app_list:
            counter += 1
            if line[0] == "#":
                # We don't care about commented out lines.
                continue
            match = group_start.search(line)
            if match:
                if curr_group is not None:
                    raise IncorrectAppsListError("There is new group started\
                                                    and previous is still not\
                                                   closed.")
                curr_group = AppsGroup(match.group()[2:-2])
                continue

            match = group_end.search(line)
            if match:
                groups.append(curr_group)
                curr_group = None
                continue

            match = description.search(line)
            if match:
                app_descr = match.group()[2:-2]
                match = just_app_name.search(line)
                app_name = match.group()
                app = App(app_name, app_descr)
                curr_group.add_application(app)
                continue

            match = just_app_name.search(line)
            if match:
                app_name = match.group()
                app = App(app_name)
                curr_group.add_application(app)
                continue

            print("Could not match any of the regex, check if line nr. " +
                  str(counter) + " in file " + file_name + " is correct.",
                  file=sys.stderr)


    return groups


def install_offical_repos_apps():
    """Display to user and install chosen apps from
    ./apps_list/arch_repo_apps.txt"""
    groups = parse_apps_list("apps_list/arch_repo_apps.txt")

def main():
    """Function which is called, when script is executed directly and not used
    as a library."""
    #install_yay()
    install_offical_repos_apps()

if __name__ == "__main__":
    main()
