#!/usr/bin/env python

import argparse, os

def replace_in_file(filename, old, new):
    with open(filename, 'r') as f:
        content = f.read()
    with open(filename, 'w') as f:
        f.write(content.replace(old, new))



def hard_coded_dirty_hacks():
    #replace_in_file("network", "ifname 'wan'", "ifname 'eth0.7'")
    #replace_in_file("network", "ifname 'wan6'", "ifname 'eth0.7'")
    replace_in_file("network", "config interface 'lan'\n\toption ifname 'wlan0'\n\toption proto 'none'", "")
    replace_in_file("network", "config interface 'lan'\n\toption ifname 'wlan1'\n\toption proto 'none'", "")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder')
    args = parser.parse_args()

    os.chdir(args.folder)
    hard_coded_dirty_hacks()

if __name__ == "__main__": main()
