#!/bin/bash



set -e

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Stopping existing gunicorn processes..."
pkill -f "gunicorn" || true

echo "Starting Flask API..."
nohup gunicorn -w 4 -b 0.0.0.0:5000 app:app > gunicorn.log 2>&1 &

echo "Deployment completed successfully!"
echo "Access your API at: http://20.110.184.202:5000"