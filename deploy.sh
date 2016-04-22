#!/bin/bash

# ---- Start config section

USER=root
HOST=10.1.0.1

ROUTER=$USER@$HOST
#ROUTER=yak

REQUIREMENTS=$(cat requirements.txt)

# ---- End config section

for req in $REQUIREMENTS; do
    echo "Requirement: $req"
done

#scp ./etc/config/* $ROUTER:/etc/config/
#ssh $ROUTER 'reboot'

