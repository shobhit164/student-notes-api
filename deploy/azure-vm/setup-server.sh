#!/usr/bin/env bash
set -euo pipefail

sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip rsync

sudo mkdir -p /opt/student-notes-api
sudo chown -R "$USER":"$USER" /opt/student-notes-api

echo "Azure VM base setup complete."

