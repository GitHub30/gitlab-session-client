#!/usr/bin/env python3

import os
import json
import requests
import argparse


def get_session(fqdn, username, password):
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gitlab-%s.json' % username)
    if os.path.exists(credential_path):
        with open(credential_path, 'r') as f:
            return json.load(f)
    else:
        r = requests.post('http://%s/api/v4/session?login=%s&password=%s' % (fqdn, username, password))
        if r.status_code == requests.codes.created:
            with open(credential_path, 'w') as f:
                f.write(r.text)
            return r.json()
        else:
            print('Cloud not get session from GitLab.')
            print(r.text)
            exit(1)


def main():
    parser = argparse.ArgumentParser(description='Obtain the session from GitLab.')
    parser.add_argument('--fqdn', required=True, help='Fully Qualified Domain Name')
    parser.add_argument('--username', '-u', required=True)
    parser.add_argument('--password', '-p', required=True, help='This arg from command line is insecure.')
    parser.add_argument('--key')
    args = parser.parse_args()

    session = get_session(args.fqdn, args.username, args.password)
    if args.key is not None:
        print(session[args.key])
    else:
        print(session)

if __name__ == '__main__':
    main()
