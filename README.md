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

The BaseController extends functionality to the NetworkController or FileController based on the subparser argument. This in turn, maps the action argument to a FileUtil or NetworkUtil method, executing the logic and obtaining a response. We then pass this response to the Logger.

