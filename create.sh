#!/bin/bash

source ~/.pyvenv/playground-3.5/bin/activate


./test_config.py ./autoconf.json | less
netjsonconfig --config autoconf.json --backend openwrt --method generate > autoconf.tar.gz   &&   tar -xf autoconf.tar.gz  &&  rm tar -xf autoconf.tar.gz
#./afterburner.py ./etc/config/


cp manual_config/dhcp ./etc/config/


