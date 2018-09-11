#!/bin/bash
# Currently only works with bash.
# Should be run from initial_config directory directly.

# Set up aliases.
echo "source $PWD/shell_files/aliases" >> ~/.bash_profile
# Set up PATH.
echo "source $PWD/shell_files/path" >> ~/.bash_profile

# Enable thefuck.
fuck
fuck
