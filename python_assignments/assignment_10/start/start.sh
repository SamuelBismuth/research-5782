#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

sudo killall -9 python3 2>/dev/null

bash $DIR/backend.sh
bash $DIR/frontend.sh