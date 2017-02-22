import feedhashcalculator, loadfeedsfromfile


# Should return boolean assertion if feeds have been changed
def checkIfFeedChanged(feedSourceList, arrayOfFeedHashes):
    calculatedHashList = getFeedHashes(feedSourceList)
    print(calculatedHashList)

def getFeedHashes(feedSourceList):
    calculatedHashList = []
    for feedSource in feedSourceList:
        for story in feedSource.entries:
            calculatedHash = feedhashcalculator.calculateHashArrayFromFeeds(story.title)
            calculatedHashList.append(calculatedHash)


def main():
    feedSourceList = loadfeedsfromfile.getFeedList()
    feedHashes = []
    feedHashes.append(getFeedHashes(feedSourceList))
    print(feedHashes)

if __name__ == '__main__':
    main()
