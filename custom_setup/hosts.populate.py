#!/usr/bin/env python

template = """
config host
	option name '{hostname}'
	option mac '{mac}'
	option ip '{ip}'
	option hostid '{ipv6_host_suffix}'
"""

data = """
34:17:eb:c4:5d:73	10.1.0.18	esxi
b0:48:7a:b3:31:93	10.1.0.34	schaltbox
f8:1a:67:4c:f8:6a	10.1.0.35	waltbox
2c:30:33:9c:46:19	10.1.0.36	kalkbox
ec:08:6b:66:4f:53	10.1.0.37	haltbox
00:10:75:29:96:c8	10.1.0.42	goflex
02:01:00:00:00:84	10.1.0.44	freenas
00:c0:08:88:22:0f	10.1.0.47	udoo
00:1e:06:33:2d:1a	10.1.0.48	odroidc2
00:1b:a9:98:64:c8	10.1.0.53	hl2250dn
ac:18:26:75:8e:5f	10.1.0.54	xp810
00:80:92:d6:3b:a7	10.1.0.55	ql710w
7c:2f:80:0f:87:f7	10.1.0.61	dl500a
7c:2f:80:02:96:44	10.1.0.62	dx600a
#18:1a:67:11:02:22	10.1.0.222	shark
9c:c7:a6:be:cf:29	10.1.0.223	fb7490
00:1c:4a:1c:ff:73	10.1.0.224	fb7270
4c:e6:76:4f:61:b2	10.1.0.225	cluster-router
f8:d1:11:a0:05:44	10.1.0.226	fusebox-router
98:90:96:ae:48:63	10.1.1.1	owl
68:05:ca:2f:4e:8d	10.1.1.2	owl
e0:f8:47:41:d6:c2	10.1.1.3	elk
f8:b1:56:b3:2a:79	10.1.1.5	gnu
28:37:37:47:7d:6e	10.1.1.21	airport-express
40:0e:85:83:5f:a4	10.1.2.1	s4active-philipp
cc:78:5f:e9:52:ea	10.1.2.21	ipad-philipp
bc:92:6b:6e:60:94	10.1.2.22	ipad-doro
b8:27:eb:94:4a:06	10.1.3.11	ut61epi
00:30:f1:ed:f9:43	10.1.3.12	surveillancepi
e8:94:f6:48:cc:f2	10.1.4.11	inet-probe-01
64:66:b3:ce:15:9a	10.1.4.12	inet-probe-02
"""

data = data.strip()

for line in data.split('\n'):
    if line.startswith('#'): continue
    mac, ip, name = line.split('\t')
    ip_parts = ip.split('.')
    ipv6_host_suffix = '::' + ip_parts[1] + ip_parts[2] + ':' + ip_parts[3]
    print(template.format(hostname=name, mac=mac, ip=ip, ipv6_host_suffix=ipv6_host_suffix))

