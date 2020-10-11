# RedCan EDR Agent tools

This repository contains a CLI to handle file management and network management using the 'argparse' Python library.

## File Manager
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

## Network Manager
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

### Architecture
The BaseController extends functionality to the NetworkController or FileController based on the subparser argument. This in turn, maps the action argument to a FileUtil or NetworkUtil method, executing the logic and obtaining a response. We then pass this response to a Logger.

## Parser
The Parser class uses the argparse library to parse command line arguments. Calling a parser instance will return a Parser object where the attribute `parsed_args` will contain the Namespace object returned from `argparse.parse_args()` method.

## Controllers
There are three controllers in this project. The BaseController can be initialized with the `parsed_args` attribute from the parser. The initializer will act as a factory, calling either the NetworkController or FileController and assigning the result of the actions to attributes.

## Utilities
The actions requested to create, modify, and delete a file are contained within the FileUtil class, which is accessed by the FileController. The actions requested to connect to a server, send data, and close a connection are contained within the NetworkUtil class, which is accessed by the NetworkController.

## Loggers
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

