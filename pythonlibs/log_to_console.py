from robot.api import logger

debug = True
def write_to_console(s):
    if debug == True:
        logger.console(s)
