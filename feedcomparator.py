def compareFeedSourceLists(feedSourceList1, feedSourceList2):
    uniqueFeedSourceList = []
    for story2 in feedSourceList2.entries:
        found = 0
        for story1 in feedSourceList1.entries:
            if story1.title == story2.title:
                found = True
                break;
        if not found:
            uniqueFeedSourceList.append(story2)
    return uniqueFeedSourceList

def compareFeedSourceLists2(feedSourceList1, feedSourceList2):
    uniqueFeedSourceList = []
    for feedSource in feedSourceList2:
        found = 0
        for story1 in feedSourceList1.entries:
            if story1.title == story2.title:
                found = True
                break;
        if not found:
            uniqueFeedSourceList.append(story2)
    return uniqueFeedSourceList

def compareFeedSources(feedSource1, feedSource2):
    uniqueEntryList = []
    for entry2 in feedSource2.entries:
        for entry1 in feedSource1.entries:
            if entry2.title == entry1.title:
                found = True
                break;
            if not found:
                uniqueEntryList.append(entry2)
            return uniqueEntryList
