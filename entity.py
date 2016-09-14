# Local modules
from base import Animal

# Global modules
import logging
from xlog import OurLogger

# Register our logger.
logging.setLoggerClass(OurLogger)
my_logger = logging.getLogger("main.entity")

class Pet(Animal):
    def __init__(self, name):
        my_logger.debug('Class instance call.')
        self.name = name

    def get_name(self):
        my_logger.info('ANIMAL name is {0}'.format(str(self.name)))

class Dog(Pet):
    def __init__(self, name):
        my_logger.debug('Class instance call.')
        self.name = name

    def make_sound(self):
        my_logger.debug('method request')
        print "Hav! Hav!"

    def get_name(self):
        my_logger.info('PET name is {0}'.format(str(self.name)))

def third_party():
    my_logger.info("Initial message from: %s!" % ("__THIRD_PARTY"))

def another_function():
    my_logger.warn("Message from: %s" % ("__ANOTHER_FUNCTION"))

if __name__ == '__main__':
    print "[Tests NOT implemented yet.]"
