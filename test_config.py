#!/usr/bin/env python

import argparse, json
import netjsonconfig

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('configfile')
    args = parser.parse_args()

    with open(args.configfile, 'r') as f:
        config = json.load(f)
    conf = netjsonconfig.OpenWrt(config, templates=[], context={})
    conf.generate()
    content = conf.render()

    print(content)

if __name__ == "__main__": main()
