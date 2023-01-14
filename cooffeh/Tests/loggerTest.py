from Modules.logger import info, debug, error
from Tests.tools import checkIfFileCreated

def testingLogInfo():
    info('testingLogInfo', '0', 'Testing if the logger.info can create the log')
    return checkIfFileCreated('./Log/log.txt', 'testingLogInfo')

def testingLogDebug():
    text = 'Testing if the logger.debug can create the log'
    debug(text)
    return checkIfFileCreated('./Log/debug.txt', 'testingLogDebug')

def testingLogError():
    try:
        t = 0
        t += 't'
    except Exception as err:
        error(err, 'testingLogError', '0', 'Testing if the logger.error can create the log')
        return checkIfFileCreated('./Log/error.txt', 'testingLogError')
