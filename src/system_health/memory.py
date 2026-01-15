

from src.system_health.cpu import get_cpu_usage, get_cpu_usage_per_job
from  utilites.exception import exception_handler
from utilites.create_logger  import create_logger
from datetime import timedelta


import psutil


def get_memory_usage():
    """
   
    Retrieves the memory usage

    returns: {memory_term: usage} otheriwse  an exception that arises or None

    """

    try:
        logger=create_logger( )
        memory_usage=psutil.virtual_memory()
        logger.info(f"Memory usage retrieved successfully: \n \t \t \t{memory_usage}")
        #convert the object fields to a dictionary if the object is not none and is also a named tuple

        memory_usage=memory_usage._asdict()
        return memory_usage
        return None
        
    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None


if __name__=="__main__":
    memory_info=get_memory_usage()
    if memory_info:
        print(memory_info)
        print(type(memory_info))