from  utilites.exception import exception_handler
from utilites.create_logger  import create_logger
from datetime import timedelta


import psutil


def get_cpu_usage():
    """
   
    Retrieves the cpu usage

    returns: {cpu_term: usage} otheriwse  an exception that arises or None

    """

    try:
        logger=create_logger( )
        cpu_usage=psutil.cpu_percent(interval=1)
        logger.info(f"CPU usage retrieved successfully: {cpu_usage}%")
        return {"cpu_usage":cpu_usage}
    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None


 
def get_cpu_usage_per_job():
    """
   
    Retrieves the cpu usage per the job that is keeping the cpu busy

    returns: {cpu_term: usage} otheriwse  an exception that arises or None

    """

    try:
        logger=create_logger( )
        cpu_usage=psutil.cpu_times()
        if not cpu_usage:
            raise ValueError("Failed to retrieve CPU usage per job.")
        
        #convrert the object fields to a dictionary
        cpu_usage_dict=cpu_usage._asdict()
        for key, value in cpu_usage_dict.items():
            #convert the time from seconds to timedelta for better readability
            cpu_usage_dict[key]=timedelta(seconds=value)
            
        logger.info(f"CPU usage  in hours per job retrieved successfully  \n: {cpu_usage_dict}")
        return cpu_usage_dict
    
    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None

if __name__=="__main__":
    cpu_info=get_cpu_usage()
    cpu_per_job=get_cpu_usage_per_job()
    if cpu_info:
        print(f"CPU Usage: {cpu_info}")

    
    if cpu_per_job:
        print("CPU Usage Per Job:")
        for job, usage in cpu_per_job.items():
            print(f"  {job}: {usage} hours")