import logging
logging.disable(logging.CRITICAL)
logging.basicConfig(filename='hello.txt', level = logging.DEBUG, format ='%(asctime)s-%(levelname)s-%(message)s')
print(logging.debug('here we start logs'))