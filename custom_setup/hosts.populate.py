#!/usr/bin/env python

template = """
config host
	option name '{hostname}'
	option mac '{mac}'
	option ip '{ip}'
	option hostid '{ipv6_host_suffix}'
"""

hosts = """
18:66:da:0c:00:b3	10.1.0.10	eel
24:05:0f:34:4a:4d	10.1.0.12	eel-wifi
34:17:eb:c4:5d:73	10.1.0.18	esxi
b0:48:7a:b3:31:93	10.1.0.34	schaltbox
f8:1a:67:4c:f8:6a	10.1.0.35	waltbox
2c:30:33:9c:46:19	10.1.0.36	kalkbox
ec:08:6b:66:4f:53	10.1.0.37	haltbox
00:10:75:29:96:c8	10.1.0.42	goflex
02:01:00:00:00:84	10.1.0.44	freenas
00:0c:29:e8:41:d5	10.1.0.45	gogs
00:0c:29:7b:9b:89	10.1.0.46	snake
00:c0:08:88:22:0f	10.1.0.47	udoo
00:1e:06:33:2d:1a	10.1.0.48	k8
00:1b:a9:98:64:c8	10.1.0.53	hl2250dn
ac:18:26:75:8e:5f	10.1.0.54	xp810
00:80:92:d6:3b:a7	10.1.0.55	ql710w
28:56:5a:67:07:03	10.1.0.56	ql820nwb
00:80:77:59:8e:63	10.1.0.57	ql820nwb-wired
7c:2f:80:0f:87:f7	10.1.0.61	dl500a
7c:2f:80:02:96:44	10.1.0.62	dx600a
28:37:37:47:7d:6e	10.1.0.71	airport-express
0c:47:c9:26:b0:64	10.1.0.72	firetv
a4:77:33:a3:d5:ba	10.1.0.73	chromecast
b8:27:eb:a2:67:6d	10.1.0.74	slice
9c:c7:a6:be:cf:29	10.1.0.223	fb7490
00:1c:4a:1c:ff:73	10.1.0.224	fb7270
4c:e6:76:4f:61:b2	10.1.0.225	cluster-router
f8:d1:11:a0:05:44	10.1.0.226	fusebox-router
98:90:96:ae:48:63	10.1.1.1	owl-onboard
#68:05:ca:2f:4e:8d	10.1.1.2	owl-addon
00:1b:21:38:45:88	10.1.1.2	owl-addon	# Intel Dual ET / First port (WOL capable)
e0:f8:47:41:d6:c2	10.1.1.3	elk-wifi
c8:2a:14:07:5e:f7	10.1.1.4	elk-wired
f8:b1:56:b3:2a:79	10.1.1.5	gnu
e0:f8:47:30:be:ca	10.1.1.7	dm-wifi
cc:61:e5:14:e9:b6	10.1.1.9	doro-db-laptop	# DEFRALT857464
40:0e:85:83:5f:a4	10.1.2.1	s4active-philipp
40:0e:85:2a:6d:11	10.1.2.2	s4active-doro
CC:61:E5:14:E9:B6	10.1.2.3	lenovo-p2-phil
CC:61:E5:14:CE:5B	10.1.2.4	lenovo-p2-doro
cc:78:5f:e9:52:ea	10.1.2.21	tablet-ipad-philipp
bc:92:6b:6e:60:94	10.1.2.22	tablet-ipad-doro
08:3D:88:9D:31:05	10.1.2.23	tablet-galaxy-tab3-7-lite
50:01:D9:D8:05:48	10.1.2.24	tablet-huawei-m2
00:90:a2:3a:af:ec	10.1.2.32	sony-prst1-philipp
44:65:0d:8a:ac:6f	10.1.2.33	kindle-voyage-doro
b8:27:eb:94:4a:06	10.1.3.11	ut61epi
00:30:f1:ed:f9:43	10.1.3.12	surveillancepi
b8:27:eb:f5:c3:f9	10.1.3.13	spypi
18:fe:34:d2:71:f5	10.1.3.14	nodemcu_01
94:9f:3e:87:52:be	10.1.4.1	sonos-wz
94:9f:3e:87:18:38	10.1.4.2	sonos-ku
a0:cc:2b:f5:b8:31	10.1.4.50	tradfri-gw
00:19:af:34:7d:48	10.1.5.1	ds1054z
"""

hosts = hosts.strip()

for line in hosts.split('\n'):
    if line.startswith('#'): continue
    line, _, _ = line.partition('#')
    line = line.strip()
    mac, ip, name = line.split('\t')
    ip_parts = ip.split('.')
    ipv6_host_suffix = '::' + ip_parts[1] + ip_parts[2] + ':' + ip_parts[3]
    print(template.format(hostname=name, mac=mac, ip=ip, ipv6_host_suffix=ipv6_host_suffix))

