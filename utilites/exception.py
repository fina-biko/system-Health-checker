from create_logger import create_logger





def exception_handler(exception:Exception):
    """
    Docstring for exception_handler

    this functions helps in returning a log of  detailed excpeion inforamtion  for the developer

    and a friendly message to the user, to get the message i need to access the .args of the exception

    """
    
    logger=create_logger()
    logger.error(f"Exception occurred: {str(exception)}", exc_info=True)
    

    print(f"could not finish the task because of : {str(exception)}")


if __name__=="__main__":
    try:
        1/0

    except Exception as e:
        exception_handler(e)

    

