import feedcomparator
import loadfeedsfromfile
import signal
import sys
import time


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

    def printColor(msg, color):
        print([color + msg + CliController.ENDC])

    def getNextColor():
        CliController.colorIterator += 1
        CliController.colorIterator = CliController.colorIterator % CliController.colorList.__sizeof__()
        return CliController.colorList[CliController.colorIterator]


def quit(signal, frame):
    print(' Quitting Infoticker...')
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, quit)
    print('Starting Infoticker...');
    print('Loading list of RSS feeds...');
    controller = CliController()
    print('helloWorld', controller.OKBLUE)
    ##print(controller.printColor((str(controller.REFRESH_INTERVAL_IN_SEC), '\033[95m')))
    initialFeedSourceList = loadfeedsfromfile.getFeedList()

    # feedTitleList = feedretrieval.detectfeedchanged.getStoryTitlesOrderedByUpdated(initialFeedSourceList)

    print('Waiting for a feed to update...')
    colorIndex = 0;

    while True:
        try:
            mostRecentList = loadfeedsfromfile.getFeedList()
            newFeedSourceList = feedcomparator.compareFeedSourceLists(mostRecentList, initialFeedSourceList)

            for entry in newFeedSourceList:
                controller.printColor(entry.title, controller.getNextColor())

            initialFeedSourceList = mostRecentList

            time.sleep(CliController.REFRESH_INTERVAL_IN_SEC)
        except KeyboardInterrupt:
            break
