#!/bin/bash

# ---- Start config section

#HOST=192.168.1.1
HOST=shark
#HOST=shark-kgs
#HOST=10.1.0.1
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

echo "Deploying all files to /etc"
scp -r ./etc/* "root@[$HOST]:/etc/"

# restart firewall (forwardings) and dnsmasq (dhcp)
#ssh root@$HOST '/etc/init.d/firewall restart'
#ssh root@$HOST '/etc/init.d/dnsmasq  restart'
#ssh root@$HOST '/etc/init.d/tinc restart'

#echo "Rebooting the router"
ssh root@$HOST 'reboot'

