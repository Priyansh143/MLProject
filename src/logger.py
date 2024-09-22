import logging
import os
from datetime import datetime

LOG_FILE = F"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", #this sets format for log message and the %___ are keywords of logging lib
    level=logging.INFO, #this line sets base level of logging severity... anything below this level (INFO here) will not be captured for logging
)
