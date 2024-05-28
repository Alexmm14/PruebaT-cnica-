#!/bin/bash

cd ./DB
docker-compose up -d

cd ..

PGPASSWORD="Admin2024#" psql -h 172.30.0.3 -U postgres -p 5432 -c "CREATE DATABASE testdb;"
PGPASSWORD="Admin2024#" psql -h 172.30.0.3 -U postgres -p 5432 -d testdb -f createTables.sql
PGPASSWORD="Admin2024#" psql -h 172.30.0.3 -U postgres -p 5432 -d testdb -f createview.sql

pipenv shell
pip install -r requirements.txt
python upData.py


