#!/usr/bin/env bash

set -xe

pwd
PRIVATE_TOKEN="$(python3 gitlab_session.py --fqdn=172.17.0.2 --username=yak --password=password3 --key private_token)"
echo ${PRIVATE_TOKEN}
pwd
