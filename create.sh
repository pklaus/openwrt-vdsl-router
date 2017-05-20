#!/bin/bash

NETJSON_CONFIG=./autoconf.json

source ~/.pyvenv/playground-3.6/bin/activate

echo "Testing the netjson configuration file $NETJSON_CONFIG"
./test_config.py $NETJSON_CONFIG | less
echo "Creating the OpenWrt config from the netjson configuration file $NETJSON_CONFIG"
netjsonconfig --config $NETJSON_CONFIG --backend openwrt --method generate > tmp.tar.gz   &&   tar -xf tmp.tar.gz  &&  rm tmp.tar.gz
./afterburner.py ./etc/config/

echo "Copying the manual OpenWrt configuration files"
cp -a manual_config/etc/* ./etc/

echo "Populating snippets that need it"
./custom_setup/hosts.populate.py       > ./custom_setup/hosts.snip
./custom_setup/forwardings.populate.py > ./custom_setup/forwardings.snip

echo "Appending the custom snippets to the respective config files"
cat custom_setup/forwardings.snip >> ./etc/config/firewall
cat custom_setup/hosts.snip       >> ./etc/config/dhcp
cat custom_setup/domains.snip     >> ./etc/config/dhcp
cat custom_setup/routes.snip      >> ./etc/config/network

