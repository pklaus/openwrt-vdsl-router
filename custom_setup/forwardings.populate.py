#!/usr/bin/env python

"""
For IPv6 check:
https://wiki.openwrt.org/doc/uci/firewall#port_accept_for_ipv6
"""

template = """
config redirect
	option name '{name}'
	option src 'wan'
	option dest 'lan'
	option proto '{proto}'
	option src_dport '{src_dport}'
	option dest_ip '{dest_ip}'
	option dest_port '{dest_port}'
	option target 'DNAT'
"""

data = """
TCP	17847	10.1.0.47:22	SSH to UDOO
TCP	16748	10.1.0.47:16748	Locus-Live-Tracking to UDOO
TCP	11069	10.1.0.47:11069	ZNC to UDOO
TCP	46385	10.1.0.47:10101	HTTP-Reflector to UDOO
TCP	52321	10.1.0.47:52321	IPLogger to UDOO
TCP	80	10.1.0.47:8080	URL Shortener to UDOO
TCP	587	10.1.1.1:22 	SSH to owl (via SMTP port 587)
TCP	17832	10.1.1.1:22	SSH to owl
TCP	27166-27168	10.1.0.47:8083-8085	FHEM to UDOO
"""

data = data.strip()

for line in data.split('\n'):
    proto, src_dport, dest, name = line.split('\t')
    dest_ip, dest_port = dest.split(':')
    print(template.format(name=name, proto=proto.lower(), src_dport=src_dport, dest_ip=dest_ip, dest_port=dest_port))

