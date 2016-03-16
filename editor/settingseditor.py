import configparser
import os


class SettingsEditor:

    DefaultPaths = {"windows32": "C:\Program Files\Steam\SteamApps\common\Team Fortress 2\\tf\cfg",
                    "windows64": "C:\Program Files (x86)\Steam\SteamApps\common\Team Fortress 2\\tf\cfg",
                    "mac": "~/Library/Application Support/Steam/SteamApps/common/Team Fortress 2/tf/cfg",
                    "linux": "~/.steam/root/SteamApps/common/Team Fortress 2/tf/cfg"}

    def __init__(self):
        setup = configparser.ConfigParser()
        setup.read_file(open('editor/settings.ini'))
        self.platform = setup['User']['Platform']
        self.loc = setup['Config']['Path']

    def settings_prompt(self):
        command = input(" 1: OS \n 2: Location \n")
        if command == "1" or command.lower() == "os":
            self.change_os()
        elif command == "2" or command.lower() == "location":
            self.change_path()
        else:
            print("Not a valid option.")
            self.settings_prompt()

    def change_os(self):
        choice = input("Current OS is %s. Change? [y/n]" % self.platform)
        if choice == "y":
            oschange = configparser.ConfigParser()
            oschange.read_file(open('editor/settings.ini'))
            newos = input("Change OS to: [Windows/Mac/Linux]")
            if newos == self.platform:
                print("That is already the current OS.")
            elif newos.lower() == "windows" or newos.lower() == "mac" or newos.lower() == "linux":
                oschange['User']['Platform'] = newos
                if newos.lower() == "windows":
                    if os.path.exists('C:\Program Files (x86)'):
                        oschange['Config']['Path'] = self.DefaultPaths['windows64']
                    else:
                        oschange['Config']['Path'] = self.DefaultPaths['windows32']
                else:
                    oschange['Config']['Path'] = self.DefaultPaths[newos.lower()]
                with open('editor/settings.ini', "w") as f:
                    oschange.write(f)
                print("OS has been changed.")
                print("Config location has been reset to the default for %s." % newos)
            else:
                print("%s is not a valid choice." % newos)

    def change_path(self):
        newpath = input("Enter path to config file location: ")
        pathchange = configparser.ConfigParser()
        pathchange.read_file(open('editor/settings.ini'))
        pathchange['Config']['Path'] = newpath
        with open('editor/settings.ini', "w") as f:
            pathchange.write(f)
        print("Path to config file changed.")
        if not(os.path.exists(newpath)):
            print("Warning: %s does not exist." % newpath)
