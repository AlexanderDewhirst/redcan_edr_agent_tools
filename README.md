# RedCan EDR Agent tools

The goal of this application is to create a framework that allows us to generate endpoint activity across at least two of three supported platforms (Windows, macOS, Linux). This program will allow us to test an EDR agent and ensure it generates the appropriate telemetry.

The program should trigger the following activity:
- Start a process, given a path to an executable file and the desired (optional) command-line arguments
- Create a file of a specified type at a specified location
- Modify a file
- Delete a file
- Establish a network connection and transmit data

This log should be in a machine friendly format (e.g. CSV, TSV, JSON, YAML, etc). Each data type should contain the following information:
- Process start
    - Timestamp of start time
    - Username that started the process
    - Process name
    - Process command line
    - Process ID
- File creation, modification, deletion
    - Timestamp of activity
    - Full path to the file
    - Activity descriptor - e.g. create, modified, delete
    - Username that started the process that created/modified/deleted the file
    - Process name that created/modified/deleted the file
    - Process command line
    - Process ID
- Network connection and data transmission
    - Timestamp of activity
    - Username that started the process that initiated the network activity
    - Destination address and port
    - Source address and port
    - Amount of data sent
    - Protocol of data sent
    - Process name
    - Process command line
    - Process ID


## Architecture
This repository contains a CLI to handle file management and network management using the 'argparse' Python library. There are four class types: Parser, to act as a CLI and parse the arguments; Controller, to control the request processing; Service, to provide a way for the client to interact with some functionality in the application; and Logger, a simple framework for emitting log messages.

### Parser
The Parser class uses the argparse library to parse command line arguments. The parser contains two subparsers `file_manager` and `network_manager`, providing an interface to separate services in the application. Calling a parser instance will return a Parser object where the attribute `parsed_args` will contain the Namespace object returned from `argparse.parse_args()` method.

#### File Manager
For file management, the CLI handles the following actions using the `-a` argument:
- create
- send
- replace
- delete

The file manager CLI, a subparser (called `file_manager`) handles additional arguments:
- `-l` (or `--log_filename`) to set the output log file,
- `-f` (or `--filename`) to set the output file,
- `-d` (or `--data`) to set the data we are sending to the output file,
- `-rd` (or `--replace-data`) to set the data being replaced in the output file, 
- `-r` (or `--row`) to select the row we are replacing, and
- `-c` (or `--column`) to select the column we are replacing.
Currently, it is expected that the arguments are set correctly, for the Controller to parse the parsed arguments.

To create a file, for example:
```
python3 main.py file_manager -a create -l logfile.txt -f output.txt
```
More examples can be found in the Script Commands section.

#### Network Manager
For network management, the CLI handles the following actions using the `-a` argument:
- "connect"
- "close"
- "send"

The network manager CLI, a subparser (called `network_manager`) handles additional arguments:
- `-l` (or `--log_filename`) to set the output log file,
- `--host` to set the remote host,
- `--port` to set the server port,
- `-d` (or `--data`) to set the data we are sending.
Again, it is expected that the arguments are set correctly.

To connect to a host and port, for example:
```
python3 ./main.py network_manager -a connect -l logfile.txt --host localhost --port 4000
```
More examples can be found in the Script Commands section.

### Controllers
There are three controllers in this project: BaseController, FileController, and NetworkController. The BaseController, initialized with the `parsed_args` attribute from the Parser, implements a factory design pattern, creating an instance of the NetworkController or FileController using a common interface. These "subcontroller", the FileController and NetworkController, then call a Service class.

### Services
Services provide functionality to the application. This functionality performs some action, provides a status, and response message. The actions requested in the assessment outline to create, modify, and delete a file are contained within the FileService class. The actions requested in the assessment outline to connect to a server, send data, and close a connection are contained within the NetworkService class.

### Loggers
NOTE: Expected to change.
There are four Logger classes. The BaseLogger offers basic functionality and is encapsulated in the RequestLogger, FileLogger, and NetworkLogger. The RequestLogger, accepts arguments for `status` and `parsed_args` which formats a simple message stating whether the arguments could be processed. The FileLogger and NetworkLogger, called depending on the subparser, controller, and service requested, formats a log message with the requested arguments in the assessment outline.

### Helpers
There is one Helper class. The FileHelper class decouples the action to write to a file from the FileService class to allow the Logger to utilize the same method to write to the `log_filename` argument. The FileHelper class also decouples the action to replace within a file.

The general format of the Logger message is the following:
- username
- timestamp
- process name
- process id
- command
- status
- response message (from controller)
- logger specific details if necessary (absolute file path or host/port)

## Testing Operating Systems
This application has been developed in a macOS environment and since Docker does not have the ability to containerize macOS or Windows OS, setting up a test environment within another operating system proves difficult. The Dockerfile in the application builds an image using the official Ubuntu version 18.04 image in Docker Hub and since both macOS and Linux are built on Unix, I believe this suffices. After installing Docker, you can run the following commands to get the Linux test environment running:
```
docker build --tag <container_name>:1.0 .
```
I am using `redcan_edr_agent_tools` as my container name.

This may take a few minutes. Afterwards, you can run the image with:
```
docker run --entrypoint /bin/bash -i -t <container_name>:1.0 
```

This will open bash and allow you to test the application. The commands can be found in the Script Commands section. You can open the output file or log file with:
```
cat <filename>
```

Further testing of the network manager - To bind and listen to a socket locally, you can run:
```
python3 listener.py
```
in an open bash and run the script commands in another. This script creates a server at '127.0.0.1:4000` (or localhost port 4000).
NOTE: Currently establishing a connection in every command to the network manager.

To connect to a running docker container, to test using listener.py, you can run:
```
docker exec -it <container_id> bash
```

and you can find the container_id with:
```
docker ps
```

## Script Commands
Example file commands are as follows:
```
python3 main.py file_manager -a create -l logfile.txt -f output.txt
python3 main.py file_manager -a create -l logfile.txt -f output.csv

python3 main.py file_manager -a send -l logfile.txt -f output.txt -d "My initial data."
python3 main.py file_manager -a send -l logfile.txt -f output.csv -d "My first object."

python3 main.py file_manager -a send -l logfile.txt -f output.txt -d "My second sentence on a new line." --new-line
python3 main.py file_manager -a send -l logfile.txt -f output.csv -d "My second cell on the next row." --new-line

python3 main.py file_manager -a replace -l logfile.txt -f output.txt -rd "initial data" -d "first sentence"
python3 main.py file_manager -a replace -l logfile.txt -f output.csv -rd "object" -d "cell" --row 1 --column 1

python3 main.py file_manager -a delete -l log.txt -f output.txt
python3 main.py file_manager -a delete -l logfile.txt -f output.csv
```

Example networks command are:
```
# Shell 1
python3 listener.py
# Shell 2
python3 main.py network_manager -a connect -l logfile.txt --host localhost --port 4000
python3 main.py network_manager -a send -l logfile.txt --host localhost --port 4000 -d "Send my data."
python3 main.py network_manager -a close -l logfile.txt
```
