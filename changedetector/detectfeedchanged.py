import feedhashcalculator, loadfeedsfromfile, base64, string


# Should return boolean assertion if feeds have been changed
def checkIfFeedChanged(oldHash, newHash):
    return (oldHash == newHash)


def sanitize(subject):
    printable = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return filter(lambda x: x in printable, subject)

def getFeedHashes(feedSourceList):
    calculatedHashList = []
    for feedSource in feedSourceList:
        sortedEntries = sorted(feedSource.entries, key=lambda story: story.updated);  # sort by age
        for story in sortedEntries:
            print(story);
            sanitizedFeedTitle = sanitize(story.title)
            calculatedHash = feedhashcalculator.calculateHashArrayFromFeeds(sanitizedFeedTitle)
            calculatedHashList.append(calculatedHash)

    return calculatedHashList

def getNewest(limit):
    feedListInOrder = []
    for iterator in range(0, limit):
        return;

def main():
    feedSourceList = loadfeedsfromfile.getFeedList()
    feedHashes = []
    feedHashes.append(getFeedHashes(feedSourceList))
    print(feedHashes)

if __name__ == '__main__':
    main()
