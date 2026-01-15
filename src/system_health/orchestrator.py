
#connet the cpu nad momry into a pipeline
from src.system_health.cpu import get_cpu_usage, get_cpu_usage_per_job
from src.system_health.memory import get_memory_usage
from  utilites.exception import exception_handler
from utilites.create_logger  import create_logger
def orchestrate_system_health_check():
    """
    Orchestrates the system health check by retrieving CPU and memory usage.
    gets the cpu and memory usage by calling the respective functions from cpu and memory modules
    then combines the results into a single dictionary.

    returns: A dictionary containing CPU and memory usage information, or None if an exception occurs.
    """
    try:
        logger = create_logger()
        system_health = {}

        cpu_usage = get_cpu_usage()
        if cpu_usage is not None:
            system_health.update(cpu_usage)

        cpu_usage_per_job = get_cpu_usage_per_job()
        if cpu_usage_per_job is not None:
            system_health["cpu_usage_per_job"] = cpu_usage_per_job

        memory_usage = get_memory_usage()
        if memory_usage is not None:
            system_health.update(memory_usage)

        logger.info("System health check completed successfully.")
        logger.info(f"System Health Details: {system_health}")
        return system_health

    except Exception as e:
        print()
        print()
        exception_handler(e)
        return None
    

if __name__ == "__main__":
    health_info = orchestrate_system_health_check()
    if health_info:
        print(health_info)