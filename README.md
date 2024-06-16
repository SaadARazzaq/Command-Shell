# Command Shell

## Overview
This Python-based Command Shell is a simple CLI (Command Line Interface) application that mimics basic functionalities of a typical shell. It allows users to navigate directories, list contents, execute external commands, and customize the shell prompt.

## Features
- Change directory (`cd`)
- List directory contents (`ls`)
- Execute external commands
- Exit the shell (`exit`)
- Customize the shell prompt (`prompt`)

## Requirements
- Python 3.x

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Download or clone the shell script to your local machine.

## How to Use
1. Open your terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:
    ```sh
    python shell.py
    ```

## Commands
### `cd <directory>`
- Change the current working directory.
- Example:
    ```sh
    cd /path/to/directory
    ```

### `ls [directory]`
- List the contents of the specified directory. If no directory is specified, it lists the contents of the current directory.
- Example:
    ```sh
    ls /path/to/directory
    ```

### `exit`
- Exit the shell.

### `prompt <format>`
- Customize the shell prompt format.
- Placeholders:
  - `$PWD$`: Current working directory
  - `$HOME$`: Home directory
- Example:
    ```sh
    prompt MyShell:$PWD$> 
    ```

### Executing External Commands
- Any command not recognized as a built-in command will be executed as an external command using `subprocess.run`.
- Example:
    ```sh
    python --version
    ```

## Output Screenshots

![image](https://github.com/SaadARazzaq/Command-Shell/assets/123338307/8edf1f68-0d40-486f-a7d4-dc5160a169b5)

## Test Cases:

![image](https://github.com/SaadARazzaq/Command-Shell/assets/123338307/433dca4b-455f-4bbd-83d8-9d4bdf6a435c)
![image](https://github.com/SaadARazzaq/Command-Shell/assets/123338307/0a2fc73e-abdb-4431-89a9-fd19cf261842)

## Developer Notes
- The shell uses the `os` module for directory operations and the `subprocess` module to run external commands.
- The `self.prompt_format` variable stores the format of the shell prompt, which can be customized using the `prompt` command.
- The `handle_command` method parses user input and calls the appropriate method to handle the command.

## Future Enhancements
- Add support for more built-in commands.
- Implement command history and autocomplete features.
- Improve error handling and user feedback.

---

Enjoy using the Command Shell! If you encounter any issues or have suggestions for improvements, feel free to contribute or open an issue.
