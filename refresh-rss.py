import feedparser

# Let's only show the 20 newest
limit = 20;

# Load the feeds we are going to retrieve
rssfile = open("rss-feeds.txt");
rssFeedList = []
testUrl = "http://www.nu.nl/rss"


for url in rssfile:
	rssFeedList.append([url.strip()])

stories = feedparser.parse(testUrl)
print(stories.entries)

for story in stories.entries:
    print(story.title)

