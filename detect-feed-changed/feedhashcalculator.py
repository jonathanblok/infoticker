import hashlib


def calculateHashArrayFromFeeds(feedTitle):
    m = hashlib.md5()
    m.update(feedTitle)
    return m.hexdigest()

def main():
    #pass
    print(calculateHashArrayFromFeeds("Hallo"))
    # Any code you like

if __name__ == '__main__':
    main()


