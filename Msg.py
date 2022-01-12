'''This is a message function to slow down text'''
import time
import sys


def message(message, delay=0.050):
    for i in message:
        time.sleep(delay)
        sys.stdout.write(i)
        sys.stdout.flush()
    print("")
