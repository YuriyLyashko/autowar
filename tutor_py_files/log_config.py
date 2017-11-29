import logging

logging.basicConfig(filename='tutor_log.log',
                    level=logging.INFO,
                    datefmt='%d/%m/%Y %I:%M:%S %p',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    )