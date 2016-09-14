import entity
from entity import Dog
import logging
from logging import DEBUG
from xlog import OurLogger

# Register our logger.
logging.setLoggerClass(OurLogger)
my_logger = logging.getLogger("main")

# We still need a loggin handler.
ch = logging.StreamHandler()
my_logger.addHandler(ch)

# Confgure a formatter.
formatter = logging.Formatter('LOGGER:%(name)12s - %(levelname)7s - <%(filename)s:%(username)s:%(funcname)s> %(message)s')
ch.setFormatter(formatter)

# Example main message.
my_logger.setLevel(DEBUG)
my_logger.warn("Hi mom!")

def foo():
    my_logger.debug("Hello?")

def cmd():
    my_logger.info("Hello from %s!" % ("__CMD"))

molly = Dog('Molly')
molly.get_name()
entity.third_party()
entity.another_function()
cmd()
foo()
