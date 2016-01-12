from editor import fileeditor
import sys


def main():
    command = input("<<< ")
    if command == "exit":
        sys.exit()
    elif command == "settings":
        # TODO: Add settings functionality
        pass
    else:
        config.parse_command(command)
        main()

config = fileeditor.FileEditor()

if __name__ == "__main__":
    print("TF2 Config Editor")
    print("Enter a command, or 'help' for help.")
    main()
