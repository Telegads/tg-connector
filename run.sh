#!/bin/sh
python3 -m  uvicorn app:app --host 0.0.0.0 --port 80 --reload