#!/bin/bash
set -e

if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please install Python 3.8+"
    exit
fi

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python scripts/seed_db.py

echo "Setup complete! To run the server, use: ./scripts/run.sh"