import logging

logging.basicConfig(level=logging.INFO)
#el info al final hace que muestre desde el logging.info hacia adelante
logging.info("Arrancando programa")
logging.warning("Hace calor")
logging.error("test")
logging.critical("adios")