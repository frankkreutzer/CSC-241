def complete(abbreviation):
    'returns day of the week corresponding to abbreviation'
    days = {'Mo': 'Monday',
            'Tu':'Tuesday',
            'We': 'Wednesday',
            'Th': 'Thursday',
            'Fr': 'Friday',
            'Sa': 'Saturday',
            'Su':'Sunday'}

    return days[abbreviation]


def frequencey(itemList):
    counters = {}
    for item in itemList:
        if item not in counters: #creates item counter 
            counters[item] = 1
        else: # increment item counter
            counters[item] += 1
    return counters


def wordcount(text):
    'prints frequency of each word in text' 
    wordList = text.split() # split text into list of words
    counters ={} # dictionary of counters
    for word in wordList:   
        if word in counters: # counter for word exists
            counters[word] += 1
        else: # counter for word doesn't exist
            counters[word] = 1

    for word in counters: # print word counts
        if counters[word] == 1:
            print('{:8} appears {} time.'.format(word, counters[word]))
        else:
            print('{:8} appears {} times.'.format(word, counters[word]))
