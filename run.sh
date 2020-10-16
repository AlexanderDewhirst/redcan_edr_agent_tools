#!/bin/bash
echo "Running file manager on OS: $OSTYPE"

# File manager script
python3 main.py file_manager -a create -f output.txt -l logfile.csv

python3 main.py file_manager -a send -f output.csv -l logfile.csv -d "My first string"
python3 main.py file_manager -a send -f output.csv -l logfile.csv -d "My first string"
python3 main.py file_manager -a replace -f output.csv -l logfile.csv -rd "first" -d "second" --row 1 --column 2
python3 main.py file_manager -a send -f output.csv -l logfile.csv -d "My third string" --new-line
python3 main.py file_manager -a send -f output.csv -l logfile.csv -d "My fourth string"

python3 main.py file_manager -a delete -f output.txt -l logfile.csv


# Network manager script
## NOTE: Must start server in another shell for each command. (run `python3 listener.py`)
# python3 main.py network_manager -a connect --host localhost --port 4000
# python3 main.py network_manager -a send --host localhost --port 4000 -d "My data"
# python3 main.py network_manager -a close --host localhost --port 4000
