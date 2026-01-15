

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
       
        memory_usage=memory_usage._asdict()
        #rename the keys into more readable format if the keys exist and if not let the keys remain as they are
        key_renames={
            "total":"total_memory_bytes",
            "available":"available_memory_bytes",
            "percent":"percentage_memory_used",
            "used":"used_memory_bytes",
            "free":"free_memory_bytes",
            "active":"active_memory_bytes",
            "inactive":"inactive_memory_bytes",
            "buffers":"buffers_memory_bytes",
            "cached":"cached_memory_bytes",
            "shared":"shared_memory_bytes",
            "slab":"slab_memory_bytes"
        }
        for old_key, new_key in key_renames.items():
            if old_key in memory_usage:
                memory_usage[new_key]=memory_usage.pop(old_key)
            else:
                #retun the original key if it does not exist
                continue
                

            
        return memory_usage
        
        
    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None


if __name__=="__main__":
    memory_info=get_memory_usage()
    if memory_info:
        #print the key and value  pairs each in its own line
        for key, value in memory_info.items():
            print(f"{key}: {value}",end="\n")
       