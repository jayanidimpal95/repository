print "hello try with log and date and time"
import logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, filename='loop.log')
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')
