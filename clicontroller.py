import changedetector.detectfeedchanged,\
    changedetector.loadfeedsfromfile, \
    time, \
    feedcomparator

REFRESH_INTERVAL_IN_SEC = 10


def main():
    print('Starting InfoTicker...');
    print('Loading list of RSS feeds...');
    initialFeedSourceList = changedetector.loadfeedsfromfile.getFeedList()

    #feedTitleList = changedetector.detectfeedchanged.getStoryTitlesOrderedByUpdated(initialFeedSourceList)

    print('Waiting for a feed to update...')

    while True:
        #print('Waiting for feed to update ..');
        mostRecentList = []
        mostRecentList = changedetector.loadfeedsfromfile.getFeedList()
        newFeedSourceList = []
        newFeedSourceList = feedcomparator.compareFeedSourceLists(mostRecentList, initialFeedSourceList)

        for entry in newFeedSourceList:
            print(entry.title)

        initialFeedSourceList = mostRecentList
        time.sleep(REFRESH_INTERVAL_IN_SEC);

if __name__ == '__main__':
    main()