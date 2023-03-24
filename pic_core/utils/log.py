import logging
import logging.handlers
import os
import sys


class CoreLogging(object):
    def __init__(self, max_bytes=1000000000, backup_count=1):
        self.log_file = "pic_core.log"
        self.max_bytes = max_bytes
        self.backup_count = backup_count
        self.fmt = '%(asctime)s - %(name)s - %(funcName)s() - %(lineno)i - %(levelname)s - %(message)s'
        self._load_env()

    def _load_env(self):
        _logfile = os.environ.get('PIC_CORE_LOG_FILE', default=self.log_file)
        try:
            open(_logfile, 'a').close()
            self.log_file = _logfile

        except Exception:
            self.log_file = "pic_core.log"
            pass

        if str(os.environ.get('PIC_CORE_STREAM_LOG_LEVEL')).upper() =='INFO':
            self.stream_log_level = logging.INFO
        elif str(os.environ.get('PIC_CORE_STREAM_LOG_LEVEL')).upper() == 'DEBUG':
            self.stream_log_level = logging.DEBUG
        elif str(os.environ.get('PIC_CORE_STREAM_LOG_LEVEL')).upper() == 'WARNING':
            self.stream_log_level = logging.WARNING
        elif str(os.environ.get('PIC_CORE_STREAM_LOG_LEVEL')).upper() == 'ERROR':
            self.stream_log_level = logging.ERROR
        elif str(os.environ.get('PIC_CORE_STREAM_LOG_LEVEL')).upper() == 'CRITICAL':
            self.stream_log_level = logging.CRITICAL
        else:
            self.stream_log_level = logging.DEBUG

        if str(os.environ.get('PIC_CORE_FILE_LOG_LEVEL')).upper() =='INFO':
            self.file_log_level = logging.INFO
        elif str(os.environ.get('PIC_CORE_FILE_LOG_LEVEL')).upper() =='DEBUG':
            self.file_log_level = logging.DEBUG
        elif str(os.environ.get('PIC_CORE_FILE_LOG_LEVEL')).upper() =='WARNING':
            self.file_log_level = logging.WARNING
        elif str(os.environ.get('PIC_CORE_FILE_LOG_LEVEL')).upper() =='ERROR':
            self.file_log_level = logging.ERROR
        elif str(os.environ.get('PIC_CORE_FILE_LOG_LEVEL')).upper() =='CRITICAL':
            self.file_log_level = logging.CRITICAL
        else:
            self.file_log_level = logging.DEBUG

    def __call__(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.setLevel(self.stream_log_level)

        formatter = logging.Formatter(self.fmt)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(self.stream_log_level)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if self.log_file:
            handler = logging.handlers.RotatingFileHandler(
                self.log_file,
                maxBytes=self.max_bytes,
                backupCount=self.backup_count
            )
            handler.setLevel(self.file_log_level)
            handler.setFormatter(formatter)
            logger.addHandler(handler)

        return logger


getMyLogger = CoreLogging()
