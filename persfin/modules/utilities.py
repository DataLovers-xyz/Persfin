
def classification_engine(entry, classification_set):
    for classifier in classification_set:
        result = classify_entry(entry,classifier[0],classifier[1])
        if result != 'Not Classified':
            break
    return result

def classify_entry(entry,classifier, tag):
    result = "Not Classified"
    for element in classifier:
        if entry.lower().find(element.lower()) > 0:
            result = tag
            break
        else:
            pass
    return result
