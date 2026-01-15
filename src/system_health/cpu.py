
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

            This breaks down the "work" into specific categories so you know why the CPU is busy: 

        User: Time spent running your actual programs (e.g., Python scripts, browser).
        System: Time the CPU spent doing "office work" for the computer (e.g., managing files, talking to hardware).
        I/O Wait (Linux): Time the CPU spent sitting around waiting for a slow disk or network to finish a task. If this is high, your disk is the bottleneck, not the CPU.
        Idle: Time the CPU spent doing absolutely nothing. 
    returns: {cpu_term: usage} otheriwse  an exception that arises or None

    """

    try:
        logger=create_logger( )
        cpu_usage=psutil.cpu_times()
        if not cpu_usage:
            raise ValueError("Failed to retrieve CPU usage per job.")
        
        #convrert the object fields to a dictionary
        cpu_usage_dict=cpu_usage._asdict()
        # rename the keys into more readable format if the keys exist and if not let the keys remain as they are
        key_renames={
            "user":"cpu_user_applications",
            "system":"cpu_system_applications",
            "idle":"cpu_idle",
            "iowait":"cpu_iowaiting",
            "irq":"cpu_interrupt",
            "softirq":"cpu_softirq",
            "steal":"cpu_steal",
            "guest":"cpu_guest",
            "guest_nice":"cpu_guest_nice"
        }
        for old_key, new_key in key_renames.items():
            if old_key in cpu_usage_dict:
                cpu_usage_dict[new_key]=cpu_usage_dict.pop(old_key)
            else:
                #retun the original key if it does not exist
                continue
 
        #convert the time from seconds to timedelta for better readability
        for key, value in cpu_usage_dict.items():
            
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