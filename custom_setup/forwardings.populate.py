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
TCP	80	10.1.0.47:80	HTTP  -> UDOO nginx (Blog, URL Shortener)
TCP	443	10.1.0.47:443	HTTPS -> UDOO nginx (Gogs)
TCP	17847	10.1.0.47:22	SSH   -> UDOO
TCP	16748	10.1.0.47:16748	Locus -> UDOO (Locus-Live-Tracking)
TCP	11069	10.1.0.47:11069	ZNC   -> UDOO
TCP	25	10.1.0.47:25	SMTP  -> UDOO
TCP	46385	10.1.0.47:10101	HTTP-Reflector -> UDOO
TCP	52321	10.1.0.47:52321	IPLogger -> UDOO
TCP	27166-27168	10.1.0.47:8083-8085	FHEM -> UDOO
TCP	17842	10.1.0.42:22	SSH   -> GOFLEX
TCP	587	10.1.1.1:22	SSH   -> owl (via SMTP port 587)
TCP	17832	10.1.1.1:22	SSH   -> owl
TCP	22101	10.1.0.1:22	SSH   -> Shark
UDP	5060	10.1.0.223:5060	SIP   -> fb7490
TCP	22	10.1.0.45:22	SSH   -> gogs
"""

data = data.strip()

for line in data.split('\n'):
    proto, src_dport, dest, name = line.split('\t')
    dest_ip, dest_port = dest.split(':')
    print(template.format(name=name, proto=proto.lower(), src_dport=src_dport, dest_ip=dest_ip, dest_port=dest_port))

