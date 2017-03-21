import feedparser

def getFeedList():
    # Initialize list of feeds
    rssFeedList = []
    # Initialize list of stories
    feedSourceList = []
    # Load the feeds we are going to retrieve
    rssfile = open("changedetector/rss-feeds.txt")
    for url in rssfile:
        rssFeedList.append([url.strip()])

    for strippedUrl in rssFeedList:
        print(strippedUrl)
        feedSourceList.append(feedparser.parse(strippedUrl[0]))

    return feedSourceList
