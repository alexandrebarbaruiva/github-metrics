from configparser import ConfigParser


def get_config(section="MAIN", filename="config.ini"):
    """
    Function to retrieve all information from token file.
    Usually retrieves from config.ini
    """
    try:
        config = ConfigParser()
        with open(filename) as config_file:
            config.read_file(config_file)
        return config[section]
    except FileNotFoundError:
        print("No configuration file found, check 'config_sample.ini'")
        raise FileNotFoundError
