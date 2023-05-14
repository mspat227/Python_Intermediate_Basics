import logging

#logger configure(if we add info as level then below the logger.info will be exicuted)

logging.basicConfig(level=logging.DEBUG, filename= "log.log", filemode= "w",
                    format= "%(asctime)s - %(levelname)s - %(message)s")

#five levels of logging

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")