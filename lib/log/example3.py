import logging
import log_config

# Initialize the config
# logging.config.dictConfig(CONFIG)
logger = logging.getLogger(__name__)  # once in each module

print(__name__)
print(logger)
logger.debug("DEBUG")
logger.info("INFO")
logger.error("ERRORRRR")