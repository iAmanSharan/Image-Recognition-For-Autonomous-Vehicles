import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path  =  os.path.join(os.getcwd(),"logs")
os.makedirs(log_path , exist_ok=True)

log_file_path  = os.path.join(log_path,LOG_FILE)
logging.basicConfig(
  format="[ %(asctime)s ] %(lineno)d %(levelname)s %(message)s",
  level=logging.INFO,
  filename = log_file_path
)


if __name__ =="__main__":
  logging.info("Logging has  started")