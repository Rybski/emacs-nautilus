# emacs-nautilus

This repo provides a emacs extension for Nautilus. Based on https://github.com/harry-cpp/code-nautilus. 

## Installation

- Install dependencies (emacsclinet is needed):
```
apt-get install emacs-bin-common
```

- Install extension 
```
wget -qO- https://raw.githubusercontent.com/Rybski/emacs-nautilus/master/install.sh | bash
```

There is a install_local.sh script to install from localy cloned repo

## Uninstall Extension

```
rm -f ~/.local/share/nautilus-python/extensions/emacs-nautilus.py
```  
