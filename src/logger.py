import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # creating a file name for the log file
logs_path=os.path.join(os.getcwd(),"logs",log_file)# creates full path of the log file 
os.makedirs(logs_path,exist_ok=True)# create the "logs" directory if it doesn't exist

log_file_path=os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path,# specifies the path to the file where log messages will be written
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s - %(message)s", # defines the format for each lo meassage
    level=logging.INFO,
    
    )# in essence logging.basicConfig sets up the rules for how log messages will be generated and stored.

#if __name__=="__main__":
 #   logging.info("logging has started")

                                   #me output = [ 2025-01-22 09:22:14,041 ] 19 root -INFO - logging has started  # format 
