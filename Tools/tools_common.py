import configparser as cp


class Tools():
    def __init__(self):
        self.name = 'Tool1'

    def _folderpath(self):
        pass


def read_config() -> object:
    config = cp.ConfigParser()
    config.read(r'../config.ini', encoding='UTF-8')
    return config

if __name__ == '__main__':
    test = read_config()
    print('completed')