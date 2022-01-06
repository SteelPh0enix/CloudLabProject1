#!/bin/sh
./wait-for-it.sh database:3306 -t 0
python -m flask run --no-debugger --host 0.0.0.0 --port 8080