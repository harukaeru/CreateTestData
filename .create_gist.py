#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import os

### USAGE ###
# lay the file in your favorite path, like /path/to/
# create alias in your shell like the following.
#
# alias gistc='python /path/to/.create_gist.py' >> .bashrc
#
# Now you can just type "gistc" when it is created by this script.

### already known issue ###
# - directory is shown...

### CONSTANT ###
FRONT_TAG = '<script src="'
GIST_URL = 'http://gist-it.appspot.com/github/'

BLOB = 'blob'
MASTER = 'master'

END_TAG = '"></script>'
GIT_FILE = '.git'

### setting ###
# GitHubのユーザ名です（これはぼくの）
user = 'harukaeru'
# $Homeで打ち止めしてます（これもぼくの）
stop_loop = '/Users/usrNeko'
# ソースを出力させない拡張子です。１個しか出力しないときは効きません
ignore_ext = ['.exe', '.pyc']

# 実装まだ(´・∀・｀)
isPaste = True

### code ###
# Get the current directory
child_directory = os.getcwd()
directory = child_directory

# Search ".git" forever until it is found
while not GIT_FILE in os.listdir(directory):
    directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

    if directory == stop_loop:
        print GIT_FILE, "is not found."
        exit()

repository = directory.split("/")[-1]
sub_directory = child_directory.replace(directory, "")

# Create file path
src_link = os.path.join(GIST_URL, user, repository, BLOB, MASTER)

# Method of creating the tag. "mean" means middle.
getTag = lambda mean: FRONT_TAG + mean + END_TAG

# if argument is nothing, output all
if len(sys.argv) <= 1:
    ignore_ext += GIT_FILE
    for filename in os.listdir(child_directory):
        isIgnoreFile = False
        for ext in ignore_ext:
            isIgnoreFile |= filename.endswith(ext)

        if not isIgnoreFile:
            print getTag(os.path.join(src_link + sub_directory + '/' + filename))
    exit()
elif len(sys.argv) > 2:
    print "Arguments are too much."
    exit()

srcname = getTag(os.path.join(src_link, sys.argv[1]))
print srcname
