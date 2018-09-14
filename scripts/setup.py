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
import argparse

# Parsing apps list files.
import file_parser
# We are going to use it for linking.
from base import get_root_folder


def install_yay():
    """Installs yay AUR helper."""
    subprocess.call(["sh", "setup/install_yay.sh"])

def install_offical_repos_apps():
    """Display to user and install chosen apps from
    ./apps_list/arch_repo_apps.txt"""
    groups = file_parser.parse_apps_list("apps_list/arch_repo_apps.txt")

def get_argparser_parser(parser=argparse.ArgumentParser()):
    parser.add_argument("--parse-app-file", help="Parses file provided\
                        as an argument and pretty prints all groups.")
    parser.set_defaults(func=parse_conf)

def parse_conf(args):
    if args.parse_app_file:
        try:
            groups = file_parser.parse_apps_list(args.parse_app_file)
            for group in groups:
                group.pretty_print()
        except file_parser.AppsListParserError as e:
            print("There was an error on line: " + e.line_number)
            print("Error name: " + e.__class__.__name__)
            print("Error message: " + e.message)
        except FileNotFoundError as e:
            print("There was an error on line: N/A")
            print("Error name: " + e.__class__.__name__)
            print("Error: Could not open file " + e.filename)

def main():
    """Function which is called, when script is executed directly and not used
    as a library."""
    main_parser = argparse.ArgumentParser("Main utility for setting up fresh\
                                          Arch Linux.")

    subparsers = main_parser.add_subparsers(help="Subcommands for utility.")

    parser_parser = subparsers.add_parser("parse")
    get_argparser_parser(parser_parser)

    args = main_parser.parse_args()
    args.func(args)
    #install_yay()
    #install_offical_repos_apps()

if __name__ == "__main__":
    main()
