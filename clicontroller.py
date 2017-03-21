import changedetector.detectfeedchanged,\
    changedetector.loadfeedsfromfile, \
    time, \
    feedcomparator

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
        time.sleep(1);

if __name__ == '__main__':
    main()