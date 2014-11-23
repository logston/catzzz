"""
This is a module that will destructively insert cats into your source code at run time.
"""
import os
import random
import threading
import time
import sys

__version__ = '0.1.3'


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))


def generate_cats():
    """
    A generator that returns ASCII cats.
    """
    with open(os.path.join(CURRENT_DIR, 'ascii_catzzz.txt')) as fd:
        ascii_catzzz_lines = fd.readlines()

        cat_lines = []
        for line in ascii_catzzz_lines:
            if not line.strip():
                yield ''.join(cat_lines)
                cat_lines = []
            else:
                cat_lines.append(line)


def print_dem_catzzz():
    """
    A callable to print all of the cats.
    """
    cat_gen = generate_cats()
    for cat in cat_gen:
        print('\n' + cat)
        time.sleep(random.randint(10, 30))
    del sys.modules['catzzz']


# Start printing cats.
thread = threading.Thread(target=print_dem_catzzz)
thread.daemon = True
thread.start()