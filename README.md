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

opkg install vnstat vnstati luci-app-vnstat

In `/etc/vnstat.conf` replace:

    DatabaseDir "/var/lib/vnstat"
    # with
    DatabaseDir "/mnt/external/vnstat"
    # and
    SaveInterval 30
    # with
    SaveInterval 15
    # and
    Interface "eth0"
    # with
    Interface "pppoe-wan"

Could be done with inline change with sed:

    sed -i 's/OLD_VERSION/NEW_VERSION/g' /etc/vnstat.conf

For the vnstat system I use, I first had to initialize the db once:

    vnstat -u -i br-lan
    vnstat -u -i pppoe-wan
    vnstat -u -i eth0.7

Set up cronjob:

    echo "*/5 * * * * vnstat -u" >> /etc/crontabs/root
    /etc/init.d/cron restart

Or rather no, we don't want cron to run the manual `vnstat -u` command,
we want vnstatd to update the database (and respect our SaveInterval to write
to USB flash):

    rm /etc/crontabs/root
    rm /etc/config/vnstat
    touch /etc/config/vnstat
    /etc/init.d/vnstat enable
    /etc/init.d/vnstat start
    /etc/init.d/cron restart

Add

    #/etc/crontabs/root # nope, not anymore, see above
    /etc/vnstat.conf

to `/etc/sysupgrade.conf`

Check stats on the terminal with `vnstat --months` or
on the luci web interface at: *Status* → *VnStat Traffic Monitor*.

See:
* <https://gist.github.com/ruzickap/10016376>
* <https://wiki.openwrt.org/doc/howto/vnstat>
