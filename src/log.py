import sys

class Log():
    def __init__(self):
        pass
    def write(self, msg):
        sys.stdout.write(msg + '\n')