import changedetector.detectfeedchanged,changedetector.feedhashcalculator, changedetector.loadfeedsfromfile, \
    time, feedcomparator
def main():
    print('Starting InfoTicker...');
    print('Loading list of RSS feeds...');
    initialFeedSourceList = changedetector.loadfeedsfromfile.getFeedList()

    #feedTitleList = changedetector.detectfeedchanged.getStoryTitlesOrderedByUpdated(initialFeedSourceList)

    while True:
        print('Waiting for feed');
        mostRecentList = changedetector.loadfeedsfromfile.getFeedList()
        newFeedSourceList = feedcomparator.compareFeedSourceLists(mostRecentList, initialFeedSourceList)
        print(changedetector.getStoryTitlesOrderedByUpdated(newFeedSourceList))
        initialFeedSourceList = mostRecentList
        time.sleep(1);

if __name__ == '__main__':
    main()