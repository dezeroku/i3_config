#!/bin/bash

# Install plugin manager.
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# Download plugins.
~/.tmux/plugins/tpm/bin/install_plugins
