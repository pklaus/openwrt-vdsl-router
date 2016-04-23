#!/bin/bash

#------
# Script to backup the OpenWrt router settings
# Should be used when somethings is changed via the
# user interface to figure out how to merge it in here.
# (Otherwise, the change gets wiped out with the next deploy.)
#------


#backup-etc-dirs.py -f ./backups/ vdsl-router

# or more explicitly

backup-etc-dirs.py -f ./backups/ 10.1.0.1
