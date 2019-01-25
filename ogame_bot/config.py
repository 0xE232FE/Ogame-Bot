import json
import logging


def load_config(config_file="config.json"):
    logger = logging.getLogger("CONFIG LOADER")
    basic_error = "Error when load config file {0}".format(config_file)
    try:
        with open(config_file) as json_data_file:
            config = json.load(json_data_file)
        return config
    except ValueError as e:
        logger.error("{0} : json decoding failed ({1})".format(basic_error, e))
    except IOError as e:
        logger.error("{0} : file opening failed ({1})".format(basic_error, e))
    except Exception as e:
        logger.error("{0} : {1}".format(basic_error, e))
    return None
