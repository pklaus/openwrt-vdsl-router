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

#### VPN via tinc

* <https://tinc-vpn.org>
* <https://wiki.openwrt.org/doc/howto/vpn.tinc>
* <https://wiki.freifunk.net/Tinc>
* <http://vardump.org/wiki.php/WZR-HP-G300NH-tinc>
* <http://blog.philippklaus.de/2012/01/vpn-with-tinc-and-ipv6-using-openwrt-routers/>

First time procedure:

    /etc/init.d/tinc enable

#### USB Storage

The partition `/dev/sda1` of your first connected USB thumb drive
will be mounted with vfat file system to `/mnt/external`.
Please create /mnt/external manually before deploying.

#### vnstat

vnstat is configured to store its database in the USB stick mounted
to /mnt/external/.

Check stats on the terminal with `vnstat --months` or
on the luci web interface at: *Status* → *VnStat Traffic Monitor*.

See:
* <https://gist.github.com/ruzickap/10016376>
* <https://wiki.openwrt.org/doc/howto/vnstat>

#### Sysupgrade

Upgrade the system by flashing a new sysupgrade image (via the web interface). Deselect keep settings.
After upgrading, create a backup of the fresh configuration and put it into <https://bitbucket.org/pklaus/openwrt-configurations/branches/>
Then, deploy the proper configuration:
* Deploy configuration files
* Reboot (to get PPPoE connection)
* Deploy again, this time installing the packages with opkg.
* Reboot again.
* Deploy again, this time configuring fstab, vnstat and the likes
* Reboot again.

#### VLAN -> DMZ

*Only planned, not implemented so far!!!*

in DMZ 1 (VLAN 111):

* Nginx reverse proxy server with own websites

in DMZ 2 (VLAN 222):

* FHEM
* fusebox router
* WiFi AP for FHEM/fusebox/mqtt clients

