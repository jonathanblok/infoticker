import feedhashcalculator, loadfeedsfromfile, base64, string


# Should return boolean assertion if feeds have been changed
def checkIfFeedChanged(feedSourceList, arrayOfFeedHashes):
    calculatedHashList = getFeedHashes(feedSourceList)
    print(calculatedHashList)

def sanitize(subject):
    printable = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return filter(lambda x: x in printable, subject)

def getFeedHashes(feedSourceList):
    calculatedHashList = []
    for feedSource in feedSourceList:
        for story in feedSource.entries:
            sanitizedFeedTitle = sanitize(story.title)
            calculatedHash = feedhashcalculator.calculateHashArrayFromFeeds(sanitizedFeedTitle)
            calculatedHashList.append(calculatedHash)

    return calculatedHashList


def main():
    feedSourceList = loadfeedsfromfile.getFeedList()
    feedHashes = []
    feedHashes.append(getFeedHashes(feedSourceList))
    print(feedHashes)

if __name__ == '__main__':
    main()
