#!/bin/bash

# Remove previous version and setup folder
echo "Removing previous version (if found)..."
mkdir -p ~/.local/share/nautilus-python/extensions
rm -f ~/.local/share/nautilus-python/extensions/emacs-nautilus.py

# Download and install the extension
echo "Downloading newest version..."
cp ./emacs-nautilus.py ~/.local/share/nautilus-python/extensions/emacs-nautilus.py

# Restart nautilus
echo "Restarting nautilus..."
nautilus -q

echo "Installation Complete"
