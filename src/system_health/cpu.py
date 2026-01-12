from  utilites.exception import exception_handler
from utilites.create_logger  import create_logger


import psutil


def get_cpu_usage():
    """
   
    Retrieves the cpu usage

    returns: {cpu_term: usage} otheriwse  an exception that arises or None

    """

    try:
        cpu_usage=psutil.cpu_percent(interval=1)
        return {"cpu_usage":cpu_usage}
    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None


if __name__=="__main__":
    cpu_info=get_cpu_usage()
    if cpu_info:
        
        print(f"CPU Usage: {cpu_info['cpu_usage']}%")
