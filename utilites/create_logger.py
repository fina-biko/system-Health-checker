
import logging

path="logs/app.log"

def create_logger(level=logging.INFO):
    """
    creates a logger object to log messages to a file

    args: None

    returns: logger object
    """

    logger=logging.getLogger(__name__)

    #add levler to logger
    logger.setLevel(logging.INFO)

    #add handler to logger
    handler=logging.FileHandler(path)
    handler.setLevel(logging.INFO)

    #add formatter to handler
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

   #add handler to logger then return logger object
    logger.addHandler(handler)
    return logger




if __name__=="__main__":
    log=create_logger()
    #once we create the logger object, we call the info method to log messages
    log.info("logger created successfully")