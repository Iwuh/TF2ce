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

    def add_line(self):
        classestoedit = input("Input the config files you'd like to edit, separated by spaces. 1-9 for classes, "
                              "0 for autoexec: ")
        texttoadd = input("Enter the line you'd like to append: ")
        for i in classestoedit:
            with open(self.loc + "/%s.cfg" % self.MercDict[i], "a+") as f:
                f.write("")
                f.write(texttoadd)
