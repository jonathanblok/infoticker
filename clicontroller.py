import feedretrieval.detectfeedchanged,\
    feedretrieval.loadfeedsfromfile, \
    time, \
    feedcomparator, \
    sys, \
    signal

REFRESH_INTERVAL_IN_SEC = 10

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printColor(msg, color):
    print(color + msg + bcolors.ENDC);

def quit(signal, frame):
    print(' Quitting Infoticker...');
    sys.exit(0)

def main():
    print('Starting Infoticker...');
    print('Loading list of RSS feeds...');
    initialFeedSourceList = feedretrieval.loadfeedsfromfile.getFeedList()

    #feedTitleList = feedretrieval.detectfeedchanged.getStoryTitlesOrderedByUpdated(initialFeedSourceList)

    print('Waiting for a feed to update...')

    while True:
        try:
            #print('Waiting for feed to update ..');
            mostRecentList = []
            mostRecentList = feedretrieval.loadfeedsfromfile.getFeedList()
            newFeedSourceList = []
            newFeedSourceList = feedcomparator.compareFeedSourceLists(mostRecentList, initialFeedSourceList)

            for entry in newFeedSourceList:
                print(entry.title)

            initialFeedSourceList = mostRecentList

            time.sleep(REFRESH_INTERVAL_IN_SEC)
        except KeyboardInterrupt:
            break

if __name__ == '__main__':
    signal.signal(signal.SIGINT, quit)
    main()