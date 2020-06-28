import logging

# Variable logger a utilizar
logger = logging

logger.basicConfig(
    level    =logging.DEBUG,
    format   ='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt  ='%I:%M:%S %p',
    handlers =[
        logging.FileHandler('logger_datos.log'),
        logging.StreamHandler()
    ]
)