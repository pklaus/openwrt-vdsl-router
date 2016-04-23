#!/bin/bash

# ---- Start config section

HOST=10.1.0.1
#HOST="2003:1234:5678:9abc::1"
#HOST=yak
PACKAGE_FILE=custom_setup/additional_packages.lst

# ---- End config section

REQUIREMENTS=$(cat $PACKAGE_FILE | grep -v '^#')

ssh root@$HOST "opkg update"
for req in $REQUIREMENTS; do
    echo "Requirement: $req"
    ssh root@$HOST "opkg install $req"
done

scp ./etc/config/* "root@[$HOST]:/etc/config/"
ssh root@$HOST 'reboot'

