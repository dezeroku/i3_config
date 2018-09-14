"""Initial installation and setup of my Arch Linux config.
Should handle installing packages and linking up some dotfiles.

Steps:
    Install AUR helper (yay currently) Ok
    Install stuff Ok (parse file needs some improvement)
    Install AUR stuff Ok
    Some setup for npm
    Link dotfiles
    Install language packages (go, python, js etc.)
    Configure MIME and let apps update their plugins or whatever
    Configure thefuck
    add required shell sources
    Enable vnstat
By d0ku 2018"""

import subprocess
import argparse
import sys

# Parsing apps list files.
import file_parser
# We are going to use it for linking.
from base import get_root_folder


def install_yay():
    """Installs yay AUR helper."""
    result = subprocess.run(["sh", "setup/install_yay.sh"])
    return result

def install_offical_repos_apps():
    """Display to user and install chosen apps from
    ./apps_list/arch_repo_apps.txt"""
    groups = file_parser.parse_apps_list("apps_list/arch_repo_apps.txt")

def get_argparser_parser(parser=argparse.ArgumentParser()):
    parser.add_argument("--parse-app-file", help="Parses file provided\
                        as an argument and pretty prints all groups. It should\
                        be used mainly as a tool to check whether\
                        configuration file is correct.")
    parser.set_defaults(func=parse_func)

    return parser

def get_argparser_installer(parser=argparse.ArgumentParser()):
    exsclusive = parser.add_mutually_exclusive_group()

    group = exsclusive.add_argument_group()
    group.add_argument("--install-from-file", help="Parses file provided as\
                        an argument. Displays all groups to used, and installs\
                        those apps that will be accepted by user.")
    group.add_argument("--install-command", help="Command issued to package\
                        manager preceeding apps list. (Don't add '-' to it.",
                        default="Syu")
    group.add_argument("--package-manager", help="Package manager name.\
                        That's the first argument of shell call to\
                        install.",default="pacman")

    exsclusive.add_argument("--install-aur-helper", help="Installs AUR helper\
                            basing on provided string.")

    parser.set_defaults(func=install_func)

    return parser

def get_parser_groups(file_name):
    try:
        groups = file_parser.parse_apps_list(file_name)
    except file_parser.AppsListParserError as e:
        print("There was an error on line: " + e.line_number)
        print("Error name: " + e.__class__.__name__)
        print("Error message: " + e.message)
        sys.exit(1)
    except FileNotFoundError as e:
        print("There was an error on line: N/A")
        print("Error name: " + e.__class__.__name__)
        print("Error: Could not open file " + e.filename)
        sys.exit(1)

    return groups

def main_func(args):
    """That function is called when setup.py was run without any detected
    subparser command."""
    print("This command should only be run with subcommand parameters.")
    print("Run 'python3 " + sys.argv[0] + " -h' to get more info.")

def parse_func(args):
    """Function that is called when 'parse' parser command was chosen."""
    """Parse configuration file and display found groups. Mainly used for
    checking whether configuration file is correct."""
    if args.parse_app_file:
        groups = get_parser_groups(args.parse_app_file)
        for group in groups:
            group.pretty_print()

def install_func(args):
    """Function that is called when 'install' parser command was chosen."""
    if args.install_from_file:
        groups = get_parser_groups(args.install_from_file)
        package_manager = args.package_manager
        install_command = "-" + args.install_command
        to_install_apps = []
        for group in groups:
            group.process_all()
            to_install_apps += group.accepted

        print("To install: ", end=" ")
        for app in to_install_apps:
            print(app.name, end=" ")

        print("")

        to_install_str = [app.name for app in to_install_apps]

        command = package_manager + " " + install_command + " "
        for app in to_install_str:
            command += app
            command += " "

        print("Running: " + command)

        result = subprocess.run([package_manager, install_command] + to_install_str,
                                stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr)

        if result.returncode != 0:
            print("Error: Could not install apps!")
            sys.exit(1)
    elif args.install_aur_helper:
        if args.install_aur_helper == "yay":
            result = install_yay()
            if result.returncode != 0:
                print("Error: Could not install yay.")
                sys.exit(1)
        else:
            print("Error: Currently only yay install is supported that way.")
            sys.exit(1)

def main():
    """Function which is called, when script is executed directly and not used
    as a library."""
    main_parser = argparse.ArgumentParser("Main utility for setting up fresh\
                                          Arch Linux.")
    main_parser.set_defaults(func=main_func)

    subparsers = main_parser.add_subparsers(help="Subcommands for utility.")

    parser_parser = subparsers.add_parser("parse")
    get_argparser_parser(parser_parser)
    install_parser = subparsers.add_parser("install")
    get_argparser_installer(install_parser)

    args = main_parser.parse_args()
    args.func(args)
    #install_yay()
    #install_offical_repos_apps()

if __name__ == "__main__":
    main()
