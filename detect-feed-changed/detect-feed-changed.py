import feedhashcalculator


# Should return boolean assertion if feeds have been changed
def checkIfFeedChanged(feedSourceList, arrayOfFeedHashes):
    calculatedHashList = []
    for feedSource in feedSourceList:
        print("=== " + feedSource.feed.title + " ===")
        for story in feedSource.entries:
            calculatedHash = feedhashcalculator.calculateHashArrayFromFeeds(story.title)
            calculatedHashList.append(calculatedHash)


