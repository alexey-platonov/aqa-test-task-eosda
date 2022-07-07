import logging
import os
import sys

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s (%(filename)s:%(lineno)s)',
    datefmt='%Y-%m-%d %H:%M:%S'
)
LOGGER = logging.getLogger('TESTS')
