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
        'file': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': '/app/lib/log/logfile/logfile.log'
        },
        'custom_log': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'custom',
            'filename': '/app/lib/log/logfile/logifle_custom.log'
        },
        'size_rotating_log': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': '/app/lib/log/logfile/logfile_size_rotate.log',
            'maxBytes': 1024,
            'backupCount': 0
        },
        'time_rotating_log': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': '/app/lib/log/logfile/logfile_time_rotate.log',
            'when': 'm',
            'interval': 1,
            'backupCount': 0
        }
    },
    'loggers': {
        'example1': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False
        },
        'example2': {
            'handlers': ['console', 'custom_log'],
            'level': 'DEBUG',
            'propagate': False
        },
        'app.lib.log.example3': {
            'handlers': ['console', 'size_rotating_log'],
            'level': 'DEBUG',
            'propagate': False
        }
    },
    # default loggers for all class
    'root': {
        'handlers': ['time_rotating_log'],
        'level': 'INFO'
    }
}

# Initialize the config
logging.config.dictConfig(CONFIG)

# in any file, just call import log_config will do
# then depending on the logger you want, you can do :
#   logger = logging.getLogger("example2")