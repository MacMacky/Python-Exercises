from helpers.helpers import hasLength


def splitString(string='', pattern=''):
    match = ''
    i = 0
    lengthStr = len(string)
    lenPattern = len(pattern)
    chars = []
    findStr = ''
    isDone = False
    while i <= lengthStr and not isDone:
        match = string[i:lenPattern + i]
        if i >= lengthStr:
            chars.append(findStr) if hasLength(findStr) else ''
            isDone = True
        elif match == pattern:
            chars.append(findStr) if hasLength(findStr) else ''
            findStr = ''
            i += lenPattern
        else:
            findStr += string[i]
            i += 1

    return chars
