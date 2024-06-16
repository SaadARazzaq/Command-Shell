'''

Command Shell:
Programming Language: Python
Interface: CLI based

'''

import os
import sys
import subprocess

class Shell:
    def __init__(self):
        # Initialize the shell with the home directory and default prompt format
        self.home = os.path.expanduser("~")
        self.prompt_format = "PythonShell:$PWD$ "

    def main(self):
        # Print welcome message and start the shell loop from the home directory
        print("Welcome to the Python Shell")
        os.chdir(self.home)
        self.shell_loop()

    def shell_loop(self):
        # Continuously prompt for user input and handle commands
        while True:
            cwd = os.getcwd()  # Get current working directory
            prompt = self.generate_prompt(cwd)
            try:
                user_input = input(prompt)  # Display prompt and get user input
                self.handle_command(user_input)
            except EOFError:
                break  # Exit loop on EOF
            except KeyboardInterrupt:
                print()  # Handle keyboard interrupt (Ctrl+C) gracefully
                continue

    def generate_prompt(self, cwd):
        # Generate the shell prompt by replacing placeholders with actual values
        return self.prompt_format.replace("$PWD$", cwd).replace("$HOME$", self.home)

    def handle_command(self, user_input):
        # Parse the user input and execute the appropriate command
        commands = user_input.split()
        if not commands:
            return

        cmd, *args = commands
        if cmd == "cd":
            self.change_directory(args)
        elif cmd == "ls":
            self.list_directory_contents(args)
        elif cmd == "exit":
            self.exit_shell()
        elif cmd == "prompt":
            self.set_prompt_format(args)
        else:
            self.run_external_command(cmd, args)

    def change_directory(self, args):
        # Change the current working directory, handle errors if directory does not exist
        dir = args[0] if args else os.path.expanduser("~")
        try:
            os.chdir(dir)
        except FileNotFoundError:
            print(f"cd: no such file or directory: {dir}")

    def list_directory_contents(self, args):
        # List the contents of the specified or current directory, handle errors if directory does not exist
        dir = args[0] if args else "."
        try:
            for entry in os.listdir(dir):
                print(entry)
        except FileNotFoundError:
            print(f"ls: cannot access '{dir}': No such file or directory")

    def run_external_command(self, cmd, args):
        # Execute external commands using subprocess.run, handle errors if command is not found
        try:
            subprocess.run([cmd] + args)
        except FileNotFoundError:
            print(f"{cmd}: command not found")
        except Exception as e:
            print(f"{cmd}: {e}")

    def exit_shell(self):
        # Exit the shell loop and terminate the program
        print("Exiting Python Shell")
        sys.exit(0)

    def set_prompt_format(self, args):
        # Update the shell's prompt format based on user input, provide usage information if no arguments are given
        if args:
            self.prompt_format = ' '.join(args)
        else:
            print("Usage: prompt <format>")
            print("Available placeholders: $PWD$, $HOME$")

if __name__ == "__main__":
    shell = Shell()
    shell.main()
