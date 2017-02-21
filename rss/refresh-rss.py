import feedparser

class RssProvider:

    # Let's only show the 20 newest
    limit = 20;

    # Load the feeds we are going to retrieve
    rssfile = open("rss-feeds.txt")
    # Initialize list of feeds
    rssFeedList = []
    # Initialize list of stories
    feedSourceList = []
    testUrl = "http://www.nu.nl/rss"

    # TODO: Look at timestamp and add feeds in order

    for url in rssfile:
        rssFeedList.append([url.strip()])

    for strippedUrl in rssFeedList:
        print(strippedUrl)
        feedSourceList.append(feedparser.parse(strippedUrl[0]))

    for feedSource in feedSourceList:
        print("=== " + feedSource.feed.title + " ===")
        for story in feedSource.entries:
            print(story.title)

    def calculateFeedHash(feed):
        return 0;