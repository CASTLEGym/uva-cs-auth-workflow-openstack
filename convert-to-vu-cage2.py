#!/usr/bin/env python3

import json
import sys
import os


deploy_filename = 'deploy-output.json'

global pd


def update_ips(name, control_ip, game_ip):
    nodes = pd['enterprise_built']['deployed']['nodes']
    for idx, node in enumerate(nodes):
        if node['name'] == name:
            print(f"Found {name}, updating IPs.")
            # print(f"addresses = {pd['enterprise_built']['deployed']['nodes'][idx]['addresses']}")
            pd['enterprise_built']['deployed']['nodes'][idx]['addresses'][0]['addr'] = control_ip
            pd['enterprise_built']['deployed']['nodes'][idx]['addresses'][1]['addr'] = game_ip
            print(f"addresses  = {pd['enterprise_built']['deployed']['nodes'][idx]['addresses']}")


def update_password(keyfile: str, nodename: str):
    nodes = pd['enterprise_built']['deployed']['nodes']
    for idx, node in enumerate(nodes):
        if node['name'] == nodename:
            password = os.popen(f"nova get-password {nodename} {keyfile} 2> /dev/null").read()
            password = password.strip()
            print(f"Found {nodename}, updating password.")
            pd['enterprise_built']['deployed']['nodes'][idx]['password'] = password
            print(f"password = '{pd['enterprise_built']['deployed']['nodes'][idx]['password']}'")
            print("Password updated")
            return
        print(f"Examining node {node['name']}")
    print(f"Could not find node with name {nodename}")


def main():
    global pd
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} <castle-control key file>")
        return

    keyfile = sys.argv[1]

    with open(deploy_filename) as f:
        # Read the file
        pd = json.load(f)

    update_ips("dc1", "10.0.0.254", "10.10.20.254")
    update_ips("dc2", "10.0.0.253", "10.10.20.253")
    update_ips("service", "10.0.0.252", "10.10.20.252")
    update_ips("identity", "10.0.0.251", "10.10.20.251")
    update_ips("user0", "10.0.0.12", "10.10.10.10")
    update_ips("user1", "10.0.0.13", "10.10.10.11")
    update_ips("user2", "10.0.0.14", "10.10.10.12")
    update_ips("user3", "10.0.0.15", "10.10.10.13")
    update_ips("user4", "10.0.0.16", "10.10.10.14")
    update_ips("op_host0", "10.0.0.17", "10.10.30.10")
    update_ips("op_host1", "10.0.0.18", "10.10.30.11")
    update_ips("op_host2", "10.0.0.19", "10.10.30.12")
    update_ips("op_server0", "10.0.0.20", "10.10.30.20")
    update_ips("enterprise0", "10.0.0.21", "10.10.20.10")
    update_ips("enterprise1", "10.0.0.22", "10.10.20.11")
    update_ips("enterprise2", "10.0.0.23", "10.10.20.12")
    # defender: not present in workflow
    # subnet1-router: not present in workflow
    # subnet2-router: not present in workflow

    update_password(keyfile, 'dc1')
    update_password(keyfile, 'dc2')

    with open("deploy-output-vu-cage2.json", "w") as f:
        json.dump(pd, f)


if __name__ == '__main__':
    sys.exit(main())
