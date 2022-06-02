#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

sudo killall -9 python3 2>/dev/null
sudo python3 -u $DIR/../backend/server.py 8080 &