import logging
import logging.config


CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,  # allow module level config to overwrite  
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'custom': {
            'format': '%(asctime)s - [%(name)s/%(levelname)s] - [%(processname)s/%(processid)s] - %(message)s', 'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'custom_log': {
            'class': 'logging.FileHandler',
            'level': 'INFO',
            'formatter': 'custom',
            'filename': '/app/lib/log/logfile/logfile_custom.log'
        },
        'custom_error_log': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'custom',
            'filename': '/app/lib/log/logfile/logfile_custom_error.log'
        }
    },
    'loggers': {
        'example1': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False  # this will disable the root loggers
        },
        'example2': {
            'handlers': ['console', 'custom_log', 'custom_error_log'],
            'level': 'DEBUG'
        }
    },
    # default loggers for all class
    'root': {
        'handlers': ['custom_log'],
        'level': 'INFO'
    }
}

# Initialize the config
try:
    logging.config.dictConfig(CONFIG)
except Exception as e:
    pass

# logger = logging.getLogger("example1")
# logger.debug("HELLO")
# logger.info("Hello from INFO", extra={"processname": "hubdev", "processid": 123123})
"""
Result in console:
2019-11-23 01:04:39,707 - example1 - INFO - Hello from INFO   result in console

REsult in logfile
2019-11-23 01:04:39 - [example1/INFO] - [hubdev/123123] - Hello from INFO 
"""

# logger = logging.getLogger(__name__)
# logger.debug("HELLO")
# logger.info("Hello from INFO", extra={"processname": "hubdev", "processid": 123123})
"""
Result in console:
2019-11-23 01:23:58,378 - __main__ - INFO - Hello from INFO
Result in logfile
2019-11-23 01:23:58 - [__main__/INFO] - [hubdev/123123] - Hello from INFO
"""

logger = logging.getLogger("example2")
logger.debug("DEBUG DATA HERE")
logger.info(" INFO DATA HERE", extra={"processname": "hubdev", "processid": 123123})
try:
    raise Exception("Error Occured")
except Exception as e:
    logger.error('Things went wrong', extra={"processname": "hubdev", "processid": 123123}, exc_info=True)
