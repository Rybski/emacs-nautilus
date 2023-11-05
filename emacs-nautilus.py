# Emacs Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script is released to the public domain.
#
# based on https://github.com/harry-cpp/code-nautilus


from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to emacs
EMACS = 'emacsclient'

# what name do you want to see in the context menu?
EMACSNAME = 'Emacs'

# always create new window?
# NEWWINDOW = False


class EmacsExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_emacs(self, menu, files):
        safepaths = ''
        args = '-c -a \'emcas\' '

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of emacs
            # if os.path.isdir(filepath) and os.path.exists(filepath):
            #   args = ''

        # if NEWWINDOW:
        #   args = ''

        call(EMACS + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name='EmacsOpen',
            label='Open in ' + EMACSNAME,
            tip='Opens the selected files with Emacs'
        )
        item.connect('activate', self.launch_emacs, files)

        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name='EmacsOpenBackground',
            label='Open in ' + EMACSNAME,
            tip='Opens the current directory in Emacs'
        )
        item.connect('activate', self.launch_emacs, [file_])

        return [item]
