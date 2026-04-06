from logging.config import dictConfig
import logging
from pathlib import Path

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['file']
    }
})


class utilityProc():
    def __init__(self):
        super().__init__()

    @staticmethod
    def logPrint(logdata):
        logging.debug(logdata)        
        print(logdata)
        return None
    
    @staticmethod
    def load_file(filename : Path):
        try:
            return open(filename, "r")
        
        except Exception as e:
            utilityProc.logPrint("file open failed:", filename)
            utilityProc.logPrint(e)
            return None