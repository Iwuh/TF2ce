from editor import fileeditor, settingseditor
import sys


def main():
    command = input("<<< ")
    if command == "exit":
        sys.exit()
    elif command == "settings":
        settings.settings_prompt()
    elif command == "help":
        tf2ce_help()
    else:
        config.parse_command(command)
        main()


def tf2ce_help():
    print("Here is the help menu for the TF2 Config Editor. Pick an option:")
    command = input("Classes \n Commands \n exit \n")
    if command.lower() == "classes":
        print("1. Scout \n 2. Soldier \n 3. Pyro \n 4. Demoman \n 5. Heavy \n 6. Engineer \n 7. Medic \n 8. Sniper \n "
              "9. Spy")
        tf2ce_help()
    elif command.lower() == "commands":
        print("add: add 1 line to one or more config files \n read: read the contents of 1 config file \n "
              "settings: edit information like OS and config file location \n help: access the help menu")
        tf2ce_help()
    elif command.lower() == "exit":
        main()
    else:
        print("Not a valid help command.")
        tf2ce_help()

config = fileeditor.FileEditor()
settings = settingseditor.SettingsEditor()

if __name__ == "__main__":
    print("TF2 Config Editor")
    print("Enter a command, or 'help' for help.")
    main()
