#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the API
python app/app.py &

# Run tests in parallel
pytest tests/ &
wait
