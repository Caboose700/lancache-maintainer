# Lancache-Maintaner

> A small python script to purge corrupted lancache entries for Steam.

[![License](https://img.shields.io/github/license/Caboose700/lancache-maintainer)](http://badges.mit-license.org) 
![Platform](https://img.shields.io/badge/python-v3.8.1-blue) 
![Platform](https://img.shields.io/badge/platform-Linux-brightgreen)

## Description
This script reads the "access.log" created by 
"[Monolithic Game Download Cache Docker Container](https://github.com/lancachenet/monolithic)" to identify files 
which are corrupted. Corrupted files will be requested multiple times. If the script detects a file being requested five
times in a row, it will purge the file from the cache. 

## Requirements
* [Tailer Python Module](https://pypi.org/project/tailer/)
* Must be executed on machine running 
"[Monolithic Game Download Cache Docker Container](https://github.com/lancachenet/monolithic)".
* Requires "sudo" privileges as the cache directory is under the "root" user.

## Limitations
* Only watches "access.log" for "Steam" cache files.

## Configuration
File paths for the cache folder need to be changed in "main.py" if they differ from the default install 
of the "[Monolithic Game Download Cache Docker Container](https://github.com/lancachenet/monolithic)".