### vdsl-router

This repository contains my very personal DSL router configuration based
on OpenWrt on a TP-Link TL-WDR4900 and the VDSL modem DrayTek Vigor 130
set to MPoA mode.

#### PPPoE / VDSL

* [Network Setup w/ PPPoE](https://wiki.openwrt.org/doc/uci/network#protocol_pppoe_ppp_over_ethernet)

#### IPv6

* [IPv6 Setup](https://wiki.openwrt.org/doc/uci/network6)

#### regdomain fix

Another procedure I followed was the regdomain fix shown here:
<http://luci.subsignal.org/~jow/reghack/README.txt>

#### USB Storage

The partition `/dev/sda1` of your first connected USB thumb drive
will be mounted with vfat file system to `/mnt/external`.
Please create /mnt/external manually before deploying.
