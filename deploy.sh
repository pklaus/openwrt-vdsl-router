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

#ssh root@$HOST "opkg update"
#for req in $REQUIREMENTS; do
#    echo "Requirement: $req"
#    ssh root@$HOST "opkg install $req"
#done

# Deploying all configuration files to /etc
scp -r ./etc/* "root@[$HOST]:/etc/"

# Mount entries defined in /etc/config/fstab (eg. /mnt/external)
#ssh root@$HOST 'mkdir /mnt/external'
#ssh root@$HOST 'service fstab enable'
#ssh root@$HOST '/sbin/block mount'

# Setup vnstat DBs:
#ssh root@$HOST 'vnstat -u -i br-lan'
#ssh root@$HOST 'vnstat -u -i pppoe-wan'
#ssh root@$HOST 'vnstat -u -i eth0.7'
#ssh root@$HOST 'touch /etc/config/vnstat'
#ssh root@$HOST '/etc/init.d/vnstat enable'
#ssh root@$HOST '/etc/init.d/vnstat start'

# restart cron daemon
ssh root@$HOST '/etc/init.d/cron restart'
# restart firewall (forwardings) and dnsmasq (hosts, dhcp)
ssh root@$HOST '/etc/init.d/firewall restart'
ssh root@$HOST '/etc/init.d/dnsmasq  restart'
# restart the VPN daemon tinc
ssh root@$HOST '/etc/init.d/tinc restart'
# restart WiFi
ssh root@$HOST 'wifi'

#echo "Rebooting the router"
#ssh root@$HOST 'reboot'

