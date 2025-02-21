from madebyutils import logging
# Quick dirty logging
logging.debug("debug")
logging.info("info")
logging.warning("warning")

try:
    1/0
except:
    logging.error("error", exc_info=True)
    logging.critical("Why would you divided by 0")