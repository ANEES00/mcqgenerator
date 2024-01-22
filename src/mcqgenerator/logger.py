import logging
import os 
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs") 
'''creating path my combining os.getcwd and logs
for eg : c:/users/.../logs'''
os.makedirs(log_path, exist_ok = True) #create logs folder at os.getcwd()path

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO, 
        filename=LOG_FILE_PATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
