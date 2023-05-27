# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line

# Part #1 

# Part1: creat function clean_cache which creates a directory 'cache'
# if it doesn't exist, but removes all files and subfolders within 
# 'cash'-directory if it does exist.

import os, shutil
from zipfile import ZipFile


paths = os.getcwd()
# print(path)
cache = os.path.join(paths, "cache")
# print(cache)                                                     


def clean_cache():
    if os.path.exists(cache):
        shutil.rmtree(cache)
    os.mkdir("cache")

clean_cache()

# part #2

# Part2: cache_zip: takes a zip file path (str) and a cache dir 
# path (str) as arguments, in that order. The function then 
# unpacks the indicated zip file into a clean cache folder.
# You can test this with provided: "data.zip file".


def cache_zip(zip_path, cache_path):
    with ZipFile(zip_path, 'r') as datazip:
        datazip.extractall(cache_path)


# Part3: cached_files: takes no arguments and returns a list of 
# all the files in the cache. The file paths should be specified 
# in absolute terms. Search the web for what this means! No 
# folders should be included in the list. You do not have to 
# account for files within folders within the cache directory.


def cached_files():
    absolute_path = os.path.abspath("cache")
    zipfile_list = []
    for everyfile in os.scandir(absolute_path):
        if everyfile.is_file():
            zipfile_list.append(everyfile.path)

    return zipfile_list

cached_files()


# Part4: find_password: takes the list of file paths from 
# cached_files as an argument. This function should read 
# the text in each one to see if the password is in there. 
# Surely there should be a word in there to indicate the 
# presence of the password? Once found, find_password 
# should return this password string.

path_lists = cached_files()

def find_password(file_list):
    for path in file_list:
        with open(path, 'r') as file:
            file_data = file.readlines()
            for file_line in file_data:
                if 'password' in file_line.lower():
                    line = file_line[file_line.find(' '):]

                    return line.strip()

find_password(path_lists)