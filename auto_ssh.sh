#!/bin/bash
# Auto reconnect ssh tunnel with keepalive
# Create a tunnel to remote port 8888 that can be accessed via localhost port 8888

while [ true ]; do
    echo Opening SSH session
    ssh -o ServerAliveInterval=1 -o ServerAliveCountMax=30 -i ~<home directory>/.ssh/id_rsa -t -L 8888:localhost:8888 <username>@<ssh.server.net> "while [ 1 ];do date;sleep 15;done"
    echo SSH session disconnected
done
