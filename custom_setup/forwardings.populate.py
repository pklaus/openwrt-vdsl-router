#!/usr/bin/env python

"""
For IPv6 check:
https://wiki.openwrt.org/doc/uci/firewall#port_accept_for_ipv6
"""

### Forwarding

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
# Proto	Port	Destination	Name
TCP	80	10.1.0.47:80	HTTP  -> UDOO nginx (Blog, URL Shortener)
TCP	443	10.1.0.47:443	HTTPS -> UDOO nginx (Gogs)
TCP	17847	10.1.0.47:22	SSH   -> UDOO
TCP	16748	10.1.0.47:16748	Locus -> UDOO (Locus-Live-Tracking)
TCP	11069	10.1.0.47:11069	ZNC   -> UDOO
TCP	25	10.1.0.47:25	SMTP  -> UDOO
TCP	46385	10.1.0.47:10101	HTTP-Reflector -> UDOO
TCP	52321	10.1.0.47:52321	IPLogger -> UDOO
#TCP	27166-27168	10.1.0.47:8083-8085	FHEM -> UDOO
TCP	17842	10.1.0.42:22	SSH   -> GOFLEX
TCP	587	10.1.1.1:22	SSH   -> owl (via SMTP port 587)
TCP	17832	10.1.1.1:22	SSH   -> owl
TCP	22101	10.1.0.1:22	SSH   -> Shark
UDP	5060	10.1.0.223:5060	SIP   -> fb7490
UDP	5070-5079	10.1.0.223:5070-5079	VoIP voice (RTP) -> fb7490
UDP	30000-30019	10.1.0.223:30000-30019	VoIP fax         -> fb7490
TCP	22	10.1.0.45:22	SSH   -> gogs
TCP	22000	10.1.0.46:22000	Syncthing
"""

for line in data.strip().split('\n'):
    if line.strip().startswith('#'): continue
    try:
        proto, src_dport, dest, name = (substr.strip() for substr in line.split('\t'))
        dest_ip, dest_port = dest.split(':')
        print(template.format(name=name, proto=proto.lower(), src_dport=src_dport, dest_ip=dest_ip, dest_port=dest_port))
    except Exception as e:
        import logging
        logging.warning('Problem with the following line:')
        logging.warning(line)
        logging.warning(e)

### Input

template = """
config rule
	option name '{name}'
	option src 'wan'
	option proto '{proto}'
	option dest_port '{dest_port}'
	option target 'ACCEPT'
"""

data = """
# Proto	Port	Name
TCP UDP	655	tincd kgs
TCP UDP	49967	tincd camelot
"""

for line in data.strip().split('\n'):
    if line.strip().startswith('#'): continue
    try:
        proto, dest_port, name = (substr.strip() for substr in line.split('\t'))
        print(template.format(name=name, proto=proto.lower(), dest_port=dest_port))
    except Exception as e:
        import logging
        logging.warning('Problem with the following line:')
        logging.warning(line)
        logging.warning(e)
