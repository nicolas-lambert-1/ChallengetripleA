#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

sudo apt update
sudo apt install -y python3 python3-pip

pip3 install psutil

python3 -m webbrowser index.html

while true; do
    python3 monitor.py
    sleep 1  # Attendre 1 seconde avant de relancer le script (facultatif)
done

