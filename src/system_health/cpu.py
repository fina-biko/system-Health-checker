from  utilites.exception import exception_handler
from utilites.create_logger import create_logger


def get_cpu_usage():
    """
   
    Retrieves the cpu usage

    returns: {cpu_term: usage} otheriwse  an exception that arises or None

    """
