# RedCan EDR Agent tools

This repository contains a CLI to handle file management and network management using the 'argparse' Python library. The goal of this application is to create a framework that allows us to generate endpoint activity across at least two of three supported platforms (Windows, macOS, Linux). This program will allow us to test an EDR agent and ensure it generates the appropriate telemetry.

The program should trigger the following activity:
● Start a process, given a path to an executable file and the desired (optional) command-line arguments
● Create a file of a specified type at a specified location
● Modify a file
● Delete a file
● Establish a network connection and transmit data

This log should be in a machine friendly format (e.g. CSV, TSV, JSON, YAML, etc). Each data type should contain the following information:
● Process start
    ○ Timestamp of start time
    ○ Username that started the process
    ○ Process name
    ○ Process command line
    ○ Process ID
● File creation, modification, deletion
    ○ Timestamp of activity
    ○ Full path to the file
    ○ Activity descriptor - e.g. create, modified, delete
    ○ Username that started the process that created/modified/deleted the file
    ○ Process name that created/modified/deleted the file
    ○ Process command line
    ○ Process ID
● Network connection and data transmission
    ○ Timestamp of activity
    ○ Username that started the process that initiated the network activity
    ○ Destination address and port
    ○ Source address and port
    ○ Amount of data sent
    ○ Protocol of data sent
    ○ Process name
    ○ Process command line
    ○ Process ID


## Architecture
The BaseController extends functionality to the NetworkController or FileController based on the subparser argument. This in turn, maps the action argument to a FileUtil or NetworkUtil method, executing the logic and obtaining a response. We then pass this response to a Logger.

### Parser
The Parser class uses the argparse library to parse command line arguments. Calling a parser instance will return a Parser object where the attribute `parsed_args` will contain the Namespace object returned from `argparse.parse_args()` method.

### Controllers
There are three controllers in this project. The BaseController can be initialized with the `parsed_args` attribute from the parser. The initializer will act as a factory, calling either the NetworkController or FileController and assigning the result of the actions to attributes.

### Utilities
The actions requested to create, modify, and delete a file are contained within the FileUtil class, which is accessed by the FileController. The actions requested to connect to a server, send data, and close a connection are contained within the NetworkUtil class, which is accessed by the NetworkController.

#### File Manager
For file management, the CLI handles the following actions using the `-a` argument:
- "create"
- "send"
- "replace"
- "delete"

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
python3 ./main.py file_manager -a "create" -l "log.txt" -f "output.txt"
```

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
python3 ./main.py network_manager -a "connect" -l "log.txt" --host 'localhost' --port 4000
```

### Loggers
The response and status are then passed to a Logger subclass which will format a output log message sent to the `-l` or `--log_filename` argument in the command.

The general format of the Logger message is the following:
- username
- timestamp
- process name
- process id
- command
- status
- response message (from controller)
- logger specific details (absolute file path or host/port)

## Testing Operating Systems
This application has been developed in a macOS environment and since Docker does not have the ability to containerize macOS, setting up a test environment within another operating system proves difficult. The Dockerfile in the application builds a an image using the official Ubuntu version 18.04 image in Docker Hub. After installing Docker, you can run the following commands to get the Linux test environment running:
```
docker build --tag redcan_edr_agent_tools:1.0 .
```
This may take a few minutes. Afterwards, you can run the image with:
```
docker run --entrypoint /bin/bash -i -t redcan_edr_agent_tools:1.0 
```
This will open bash and allow you to test the application. The commands can be found in the Script Commands section. You can open the output file or log file with:
```
cat <filename>
```

## Script Commands
Example commands are as follows:
```
python3 ./main.py file_manager -a "create" -l "log.txt" -f "output.txt"
python3 ./main.py file_manager -a "send" -l "log.txt" -f "output.txt" -d "My initial data."
python3 ./main.py file_manager -a "replace" -l "log.txt" -f "output.txt" -d "updated data." -rd "initial data." -r 1 -c 1
python3 ./main.py file_manager -a "delete" -l "log.txt" -f "output.txt"
python3 ./main.py network_manager -a "connect" -l "log.txt" -h "localhost" -p "4000"
python3 ./main.py network_manager -a "send" -l "log.txt" -h "localhost" -p "4000" -d "Send my data."
python3 ./main.py network_manager -a "close" -l "log.txt"
```
