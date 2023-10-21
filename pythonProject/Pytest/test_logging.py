import logging

logger = logging.getLogger(__name__)

filehandler = logging.FileHandler("logfile.log")

logger.addHandler(filehandler)  # filehandler object

logger.debug("A debug statement is executed") # just like print statement
logger.info("Information statement")
logger.warning("Something is in warning mode")
logger.error("A Major error has happened ")
logger.critical("Critical issue")