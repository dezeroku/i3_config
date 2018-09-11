#!/bin/bash
# Currently only works with bash.
# Should be run from initial_config directory directly.

# Set up aliases.
echo "source $PWD/shell_files/aliases" >> ~/.bashrc
# Set up PATH.
echo "source $PWD/shell_files/path" >> ~/.bashrc

# Enable thefuck.
fuck
fuck
