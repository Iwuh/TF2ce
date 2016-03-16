import configparser


class FileEditor:
    """Class used to add to, remove from, read, etc .cfg files from TF2."""

    MercDict = {"1": "scout", "2": "soldier", "3": "pyro", "4": "demoman", "5": "heavyweapons",
                "6": "engineer", "7": "medic", "8": "sniper", "9": "spy", "0": "autoexec"}

    def __init__(self):
        setup = configparser.ConfigParser()
        setup.read_file(open('editor/settings.ini'))
        self.loc = setup['Config']['Path']

    def parse_command(self, command):
        if command == "add":
            self.add_line()
        elif command == "read":
            self.read_file()
        else:
            print("\"%s\" is not a valid command." % command)

    def add_line(self):
        classestoedit = input("Input the config files you'd like to edit, separated by spaces. 1-9 for classes, "
                              "0 for autoexec: ")
        texttoadd = input("Enter the line you'd like to append: ")
        try:
            for i in classestoedit.split(" "):
                with open(self.loc + "/%s.cfg" % self.MercDict[i], "a+") as f:
                    f.write("")
                    f.write(texttoadd)
        except KeyError:
            print("One of those numbers doesn't correspond to a valid config file.")

    def read_file(self):
        classtoread = input("Input the config file you'd like to read. 1-9 for a class, 0 for autoexec: ")
        if len(classtoread) != 1:
            print("Can only read one file at a time.")
        else:
            try:
                with open(self.loc + "/%s.cfg" % self.MercDict[classtoread], "r") as f:
                    print(f.read())
            except KeyError:
                print("That number doesn't correspond to a valid config file.")
            except IOError:
                print("That file can't be found. Adjust the location in the settings and/or make sure the file exists.")
