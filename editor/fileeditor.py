import configparser


class FileEditor:
    """Class used to add to, remove from, read, etc .cfg files from TF2."""
    def __init__(self):
        setup = configparser.ConfigParser()
        setup.read_file(open('editor/settings.ini'))
        self.loc = setup['Config']['Path']
