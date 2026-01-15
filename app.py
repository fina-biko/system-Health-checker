#calls the orchestrator to start the process
from src.system_health.orchestrator import orchestrate_system_health_check
from  utilites.exception import exception_handler
from utilites.create_logger  import create_logger   

def main():
    try:
        #log the start of the process
        logger = create_logger()
        logger.info("Starting system health check...")

        health_info = orchestrate_system_health_check()
        if health_info:
            logger.info("System health check completed successfully.")
            logger.info(f"System Health Details: {health_info}")
            return health_info
        else:
            logger.warning("System health check failed or returned no data.")
            return None
        
    except Exception as e:
        exception_handler(e)

    
if __name__ == "__main__":
    info=main()
    print(info)
    