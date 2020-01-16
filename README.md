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


### TODO

* Not needed, also works via ICMP Redirects (on by default). Otherwise:
  Automatically add static routes to the ones pushed with DHCP:
  `dhcp-option=121,192.168.1.0/24,1.2.3.4,10.0.0.0/8,5.6.7.8`
  See https://forum.openwrt.org/viewtopic.php?id=38308
* <https://wiki.openwrt.org/doc/howto/bwmon>

#### IPv6

<http://www.heise.de/netze/artikel/OpenWRT-wuerfelt-IPv6-Praefixe-1445607.html?artikelseite=2>

radvd is not used anymore:
<https://wiki.openwrt.org/doc/uci/radvd>

Instead, odhcpd is doing the job?
<https://wiki.openwrt.org/doc/techref/odhcpd>
<https://github.com/sbyx/odhcpd>
-> Indeed, `ps w | grep odhcpd` shows the daemon to be running.

On the upstream IPv6 interface, you can set the `ifaceid` option
to override the interface identifier for adresses received via RA
when using the protocol `dhcpv6`.

Use the `ip6prefix` option on wan6:
An (additional) user-provided IPv6 prefix for distribution to clients.

Check `logread | grep odhcpd` and `/tmp/hosts/odhcpd` for debugging
info if you want to see what odhcpd is up to.

#### Hosts

Setup CNAME for owl -> owl-amt

Add option `hostid` to each host definition specifying the IPv6 suffix (like `::252:122`)!!!!

#### Fix VoIP

* <https://github.com/katallaxie/openwrt-wdr4300/tree/master/etc/asterisk>
* <https://wiki.openwrt.org/doc/howto/stun>

Firewall for SIP might need some tuning:

<https://github.com/katallaxie/openwrt-wdr4300/blob/master/etc/firewall.sip>

```
# Block 'friendly-scanner' AKA sipvicious
iptables -I input_wan_rule -p udp --dport 5060 -m string --string "friendly-scanner" --algo bm -j DROP

# iptables -t mangle -I POSTROUTING -p tcp -m tcp --sport 22 -j DSCP --set-dscp-class cs3

# Rate limit registrations to keep us from getting hammered on
#iptables -I input_wan_rule -m string --string "REGISTER sip:" --algo bm --to 65 -m hashlimit --hashlimit 4/minute --hashlimit-burst 1 --hashlimit-mode srcip,dstport --hashlimit-name sip_r_limit -j ACCEPT

# Asterisk ports internal SIP profile
iptables -I input_wan_rule -p udp -m udp --dport 5060 -j ACCEPT
iptables -I input_wan_rule -p tcp -m tcp --dport 5060 -j ACCEPT
```
