import json
import logging
import logging.config
import log_config


with open('/app/lib/log/log_config.py', 'r') as conf:
    try:
        data = conf.read()
        print(data)
        print(type(data))
        # logging.config.dictConfig(data)
    except Exception as e:
        print("Unable to load config: %s" % e)