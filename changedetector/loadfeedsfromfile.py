import feedparser

# Let's only show the 20 newest
limit = 20;

# Initialize list of feeds
rssFeedList = []
# Initialize list of stories
feedSourceList = []
testUrl = "http://www.nu.nl/rss"

# TODO: Look at timestamp and add feeds in order

def getFeedList():
    # Load the feeds we are going to retrieve
    rssfile = open("changedetector/rss-feeds.txt")
    for url in rssfile:
        rssFeedList.append([url.strip()])

    for strippedUrl in rssFeedList:
        print(strippedUrl)
        feedSourceList.append(feedparser.parse(strippedUrl[0]))

    return feedSourceList
