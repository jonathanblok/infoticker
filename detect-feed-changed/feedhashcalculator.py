import hashlib


def calculateHashArrayFromFeeds(feedTitle):
    try:
        m = hashlib.md5()
        m.update(feedTitle)
        return m.hexdigest()
    except UnicodeEncodeError:
        print("Unencodable characters found in: "+feedTitle);

def main():
    #pass
    print(calculateHashArrayFromFeeds("Hallo"))
    # Any code you like

if __name__ == '__main__':
    main()


