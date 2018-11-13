#!/usr/bin/env python3

""" This module converts cc1 files to xyz files by removing the connectivities. """

# Imports:
import glob
import sys
import os

# Defining functions:
class FileConverter:
    
    def __init__(self, path):
        self.path = path
        
        self.choosefile()
        for name in self.files:
            self.reading(name)
            self.newfilename(name)
            self.writing()
        
    def choosefile(self):
        """ Creating a list containing all .cc1 files. """
        self.files = glob.glob(self.path)

    def reading(self, name):
        """" Storing content of selected file in an attribute of the instance. """
        with open(name, 'r') as f:
            self.lines = f.readlines()

    def newfilename(self, name):
        """ Changing extension from '.cc1' to '.xyz'. """
        self.base = os.path.splitext(name)[0]
        self.newname = str(self.base) + '.xyz'

    def writing(self):
        """ Transcribing the .cc1 files line by line using only unwanted entries. """
        with open(self.newname, 'w') as f:
            f.write(self.lines[0] + '\n')
            for l in self.lines[1:]:
                all_e = l.split()
                wanted_entries = [all_e[0],all_e[2],all_e[3],all_e[4]]
                out_line = ' '.join(wanted_entries)
                f.write(out_line + '\n')

if __name__ == '__main__':

    # Execution of the functions
    try:
        path = sys.argv[1]
    except IndexError:
        print("Please select a path following this scheme:")
        print("python converter_cc1_xyz.py '<absolute_or_relative_path/*.cc1>'")
        exit()

    convert = FileConverter(path)
    
