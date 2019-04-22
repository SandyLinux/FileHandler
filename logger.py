import logging

def createLogger(name='Node',
        flevel=logging.DEBUG,
        slevel=logging.DEBUG, # TODO: change it to ERROR in production
        formatter='%(asctime)s - %(name)s - line:%(lineno)d - [%(levelname)s] - %(message)s'):
    """
    This is a function to create a logger
    With the default setting, any log with priority higher than or equal to debug will be saved to the log file 
    any log with priority higher than or equal to  ERROR will be print out in the console
    Priorities: DEBUG < INFO < WARNING < ERROR < CRITICAL
    Usage:
        logger = createLogger('main')
        # examples to use the logger 
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')
        logger.critical('critical message')
    Args:
        name: name of the logger
        flevel: logging level for log file
        slevel: logging level for stream (console)
    Return:
        a logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(flevel)
    # create file handler that logs debug and higher level messages
    fh = logging.FileHandler('/tmp/'+name+'.log')
    fh.setLevel(flevel)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(slevel)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(formatter)
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # add the handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

if __name__=='__main__':
    hs=createLogger()
    hs.info('log info {}'.format('tailling'))
