#!/bin/bash

PROJECT_DIR="$HOME/CyberPulse"
SCRIPTS_DIR="$PROJECT_DIR/scripts"
BACKEND_DIR="$PROJECT_DIR/backend"
FRONTEND_DIR="$PROJECT_DIR/frontend"
DB_DIR="$PROJECT_DIR/db"

mkdir -p "$PROJECT_DIR" "$SCRIPTS_DIR" "$BACKEND_DIR" "$FRONTEND_DIR" "$DB_DIR"

apt update
apt install -y python3 python3-pip python3-venv jq curl git build-essential

python3 -m venv "$BACKEND_DIR/venv"
source "$BACKEND_DIR/venv/bin/activate"

pip install --upgrade pip
pip install fastapi uvicorn pydantic pymongo psycopg2-binary sqlalchemy scikit-learn

if [ ! -d "$PROJECT_DIR/node_modules" ]; then
    apt install -y nodejs npm
    cd "$FRONTEND_DIR"
    npm init -y
    npm install chart.js
fi

cd "$PROJECT_DIR"
git init

echo "{}" > "$DB_DIR/initial_schema.sql"

chmod +x "$SCRIPTS_DIR"/*.sh

echo "CyberPulse installation complete. Activate backend with 'source $BACKEND_DIR/venv/bin/activate' and run backend with 'uvicorn backend.main:app --reload'"
