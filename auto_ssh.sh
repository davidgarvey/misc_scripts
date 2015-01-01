#!/bin/bash
# Auto reconnect ssh with keepalive

while [ true ]; do
    echo Opening SSH session
    ssh -o ServerAliveInterval=1 -o ServerAliveCountMax=30 -i ~<home directory>/.ssh/id_rsa -t -L 8888:localhost:8888 <username>@<ssh.server.net> "while [ 1 ];do date;sleep 15;done"
    echo SSH session disconnected
done
