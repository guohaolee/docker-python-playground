import logging
import log_config

log = logging.getLogger("example2") 

print(log)
log.debug("HELLO FROM example2", extra={'processname': 'hub', 'processid': '129'})