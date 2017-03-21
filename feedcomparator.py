def getEntriesAsList(feedSourceList):
    entryList = []
    for feedSource in feedSourceList:
        for entry in feedSource.entries:
            entryList.append(entry)
    return entryList

def isTitleInEntryList(query, entryList):
    for entry in entryList:
        if query.title == entry.title:
            return True
    return False

def compareFeedSourceLists(feedSourceList1, feedSourceList2):
    entryList1 = getEntriesAsList(feedSourceList1)
    entryList2 = getEntriesAsList(feedSourceList2)
    uniqueEntryList = []

    for entry in entryList1:
        if not isTitleInEntryList(entry, entryList2):
            uniqueEntryList.append(entry)

    return uniqueEntryList