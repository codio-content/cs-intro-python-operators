#!/bin/bash
set -e 
set -o pipefail

. /etc/profile.d/codio-xserver.sh

$1 -m py_compile $2

nohup $@ > /dev/null 2>&1&