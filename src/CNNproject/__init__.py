import logging
import sys
import os

logs_dir = "logs"
log_file_path = os.path.join(logs_dir ,'running.log')
os.makedirs(logs_dir)

logging.basicConfig(
  level=logging.INFO,
  format="[%(asctime)s : %(level)s  : %(module)s : %(message)s]",
  handlers=[
    logging.FileHandler(log_file_path),
    logging.StreamHandler(sys.stdout)
  ]
)

logger = logging.getLogger("CNNproject")