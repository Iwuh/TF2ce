import configparser


class FileEditor(object):
    def __init__(self):
        setup = configparser.ConfigParser()
        setup.read('settings.ini')
        self.loc = setup['Config']['Path']
