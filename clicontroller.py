import feedcomparator
import loadfeedsfromfile
import signal
import sys
import time
from urllib.parse import urlparse


class CliController:

    def __init__(self):
        pass

    REFRESH_INTERVAL_IN_SEC = 10

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    colorList = [HEADER, OKBLUE, OKGREEN, WARNING, FAIL, ENDC, BOLD, UNDERLINE]
    colorIterator = -1

    def printColor(self, msg, color):
        print(color + msg + CliController.ENDC)

    def getNextColor(self):
        CliController.colorIterator += 1
        CliController.colorIterator = CliController.colorIterator % 7
        return CliController.colorList[CliController.colorIterator]

    def quit(self):
        print(' Quitting Infoticker...')
        sys.exit(0)


if __name__ == '__main__':
    print('Starting Infoticker...');
    controller = CliController()
    print('Loading list of RSS feeds...');
    initialFeedSourceList = loadfeedsfromfile.getFeedList()
    print('Waiting for a feed to update...')

    while True:
        try:
            mostRecentList = loadfeedsfromfile.getFeedList()
            newFeedSourceList = feedcomparator.compareFeedSourceLists(mostRecentList, initialFeedSourceList)

            for entry in newFeedSourceList:
                parsed_url = urlparse(entry.link)
                host_and_path = parsed_url.netloc + parsed_url.path
                controller.printColor(entry.title + ' : ' + host_and_path, controller.getNextColor())

            initialFeedSourceList = mostRecentList

            time.sleep(CliController.REFRESH_INTERVAL_IN_SEC)
        except KeyboardInterrupt:
            controller.quit()

